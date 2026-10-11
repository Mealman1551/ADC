# libadc - Archive Module
# (c) 2026 Mealman1551


import os
import zipfile
import tarfile
import py7zr
import getpass
import zlib
import pyzipper
from functools import lru_cache
from progress.bar import Bar
from cryptography.fernet import Fernet, InvalidToken

from .compression import parma_compress, parma_decompress, read_binary_file
from .crypto import derive_key_from_password
from .constants import ADC_HEADER, ADC_HEADER_V1, SALT_SIZE


class InvalidArchivePasswordError(Exception):
    """Raised when an encrypted ADC archive cannot be authenticated."""


def _normalize_path(path):
    return os.path.normcase(os.path.abspath(path))


def _list_files_in_path(path):
    normalized_path = _normalize_path(path)
    if os.path.isdir(normalized_path):
        mtime = os.path.getmtime(normalized_path)
        return _list_files_in_path_cached(normalized_path, mtime)
    return (normalized_path,)


@lru_cache(maxsize=128)
def _list_files_in_path_cached(path, mtime):
    files = []
    for root_dir, dirs, file_names in os.walk(path):
        for f in file_names:
            files.append(os.path.join(root_dir, f))
    return tuple(files)


def clear_archive_cache():
    _list_files_in_path_cached.cache_clear()


def _encode_password(password):
    if password is None:
        return None
    if isinstance(password, bytes):
        return password
    return password.encode("utf-8")


def create_adc_archive(file_paths, output_path, format="adc", password=None):
    all_files = []
    for path in file_paths:
        all_files.extend(_list_files_in_path(path))
    if format.startswith("tar"):
        mode = "w"
        if output_path.endswith(".tar.gz"):
            mode = "w:gz"
        elif output_path.endswith(".tar.xz"):
            mode = "w:xz"
        elif output_path.endswith(".tar.bz2"):
            mode = "w:bz2"
            
        with tarfile.open(output_path, mode) as tar:
            with Bar("Compressing files...", max=len(all_files)) as bar:
                for file_path in all_files:
                    tar.add(
                        file_path,
                        arcname=os.path.relpath(
                            file_path, os.path.dirname(file_paths[0])
                        ),
                    )
                    bar.next()
        print(f"TAR archive created: {output_path}")
        return

    if format == "zip":
        if password is not None:
            with pyzipper.AESZipFile(
                output_path, "w", compression=zipfile.ZIP_DEFLATED
            ) as zf:
                zf.setpassword(_encode_password(password))
                zf.setencryption(pyzipper.WZ_AES, nbits=256)
                with Bar("Compressing files...", max=len(all_files)) as bar:
                    for file_path in all_files:
                        zf.write(
                            file_path,
                            arcname=os.path.relpath(
                                file_path, os.path.dirname(file_paths[0])
                            ),
                        )
                        bar.next()
        else:
            with zipfile.ZipFile(
                output_path, "w", compression=zipfile.ZIP_DEFLATED
            ) as zf:
                with Bar("Compressing files...", max=len(all_files)) as bar:
                    for file_path in all_files:
                        zf.write(
                            file_path,
                            arcname=os.path.relpath(
                                file_path, os.path.dirname(file_paths[0])
                            ),
                        )
                        bar.next()
        print(f"ZIP archive created: {output_path}")
        return

    if format == "7z":
        with py7zr.SevenZipFile(output_path, "w") as archive:
            with Bar("Compressing files...", max=len(all_files)) as bar:
                for file_path in all_files:
                    if os.path.isdir(file_path):
                        bar.next()
                        continue
                    arcname = os.path.relpath(file_path, os.path.dirname(file_paths[0]))
                    archive.write(file_path, arcname)
                    bar.next()
        print(f"7z archive created: {output_path}")
        return

    # Handle ADC format
    use_password = password is not None
    
    # Prepare encryption if needed
    fernet = None
    salt = None
    if use_password:
        salt = os.urandom(SALT_SIZE)
        key = derive_key_from_password(password, salt)
        fernet = Fernet(key)
    
    # Create ADC archive
    with open(output_path, "wb") as archive_file:
        # Write header
        archive_file.write(ADC_HEADER_V1)
        
        # Write encryption flag
        if use_password:
            archive_file.write(b'\x01')  # encrypted flag
            archive_file.write(salt)
        else:
            archive_file.write(b'\x00')  # not encrypted flag
        
        # Write files
        with Bar("Compressing files...", max=len(all_files)) as bar:
            for file_path in all_files:
                if os.path.isdir(file_path):
                    bar.next()
                    continue

                filename = os.path.relpath(
                    file_path, os.path.dirname(file_paths[0])
                ).encode("utf-8")
                original_data = read_binary_file(file_path)
                crc32 = zlib.crc32(original_data) & 0xFFFFFFFF
                compressed_data = parma_compress(original_data)

                if use_password:
                    data_to_write = fernet.encrypt(compressed_data)
                else:
                    data_to_write = compressed_data

                archive_file.write(len(filename).to_bytes(2, "big"))
                archive_file.write(filename)
                archive_file.write(len(data_to_write).to_bytes(8, "big"))
                archive_file.write(crc32.to_bytes(4, "big"))
                archive_file.write(data_to_write)
                bar.next()
    
    print(f"ADC archive created: {output_path}")


def extract_adc_archive(archive_path, output_dir, format=None, password=None):
    """
    Extract an archive to the specified directory.
    
    Supports multiple archive formats and auto-detects ADC format versions:
    - ADC V1 (current): Header 'ADCARCH\\x01' + optional encryption + 8-byte data length + CRC32
    - ADC V0: Header 'ADCARCH\\x00' + encryption (always) + 8-byte data length
    - ADC Legacy 1.2.0: No header, plain zlib compressed files + 4-byte data length
    
    For encrypted ADC archives, prompts for password.
    
    Args:
        archive_path: Path to the archive file
        output_dir: Directory where the archive will be extracted
        format: Archive format to use. If None, auto-detects from file extension
    """
    if not format:
        if archive_path.lower().endswith((".tar", ".tar.gz", ".tar.xz", ".tar.bz2")):
            format = "tar"
        elif archive_path.lower().endswith(".7z"):
            format = "7z"
        elif archive_path.lower().endswith(".zip"):
            format = "zip"
        else:
            format = "adc"

    base_name = os.path.splitext(os.path.basename(archive_path))[0]
    dest_dir = os.path.join(output_dir, base_name)

    if format == "tar":
        os.makedirs(dest_dir, exist_ok=True)
        with tarfile.open(archive_path, "r:*") as tar:
            members = tar.getmembers()
            with Bar("Extracting files...", max=len(members)) as bar:
                for member in members:
                    tar.extract(member, path=dest_dir)
                    bar.next()
        print(f"TAR archive extracted to: {dest_dir}")
        return

    if format == "zip":
        os.makedirs(dest_dir, exist_ok=True)
        with pyzipper.AESZipFile(archive_path, "r") as zf:
            encoded_password = _encode_password(password)
            if encoded_password is not None:
                zf.setpassword(encoded_password)

            file_list = zf.namelist()
            with Bar("Extracting files...", max=len(file_list)) as bar:
                for f in file_list:
                    try:
                        zf.extract(f, path=dest_dir)
                    except RuntimeError as exc:
                        if password is None and "password" in str(exc).lower():
                            password = getpass.getpass("Enter password for archive: ")
                            encoded_password = _encode_password(password)
                            zf.setpassword(encoded_password)
                            zf.extract(f, path=dest_dir)
                        else:
                            raise
                    bar.next()
        print(f"ZIP archive extracted to: {dest_dir}")
        return

    if format == "7z":
        os.makedirs(dest_dir, exist_ok=True)
        with py7zr.SevenZipFile(archive_path, "r") as archive:
            try:
                allnames = archive.getnames()
            except Exception:
                allnames = []
            with Bar(
                "Extracting files...", max=len(allnames) if allnames else 1
            ) as bar:
                archive.extractall(path=dest_dir)
                for _ in allnames or [None]:
                    bar.next()
        print(f"7z archive extracted to: {dest_dir}")
        return

    with open(archive_path, "rb") as archive_file:
        header = archive_file.read(8)
        if header == ADC_HEADER_V1:
            # V1 format: header + encryption flag + optional salt + files
            encrypted_flag = archive_file.read(1)
            if encrypted_flag == b'\x01':
                salt = archive_file.read(SALT_SIZE)
                pwd = getpass.getpass("Enter password for archive: ")
                key = derive_key_from_password(pwd, salt)
                fernet = Fernet(key)
                encrypted = True
            else:
                encrypted = False
            has_crc = True
            data_len_bytes_count = 8
        elif header == ADC_HEADER:
            # V0 format: header + salt + encrypted files (always encrypted)
            salt = archive_file.read(SALT_SIZE)
            pwd = getpass.getpass("Enter password for archive: ")
            key = derive_key_from_password(pwd, salt)
            fernet = Fernet(key)
            encrypted = True
            has_crc = False
            data_len_bytes_count = 8
        else:
            # Legacy 1.2.0 format: no header, plain zlib compressed files (4-byte data length)
            archive_file.seek(0)
            encrypted = False
            has_crc = False
            data_len_bytes_count = 4
            fernet = None

        file_count = 0
        files_to_extract = []

        while True:
            filename_len_bytes = archive_file.read(2)
            if not filename_len_bytes:
                break
            filename_len = int.from_bytes(filename_len_bytes, "big")
            filename = archive_file.read(filename_len).decode("utf-8", errors="ignore")
            data_len_bytes = archive_file.read(data_len_bytes_count)
            data_len = int.from_bytes(data_len_bytes, "big")
            if has_crc:
                crc32_bytes = archive_file.read(4)
                crc32_expected = int.from_bytes(crc32_bytes, "big")
            else:
                crc32_expected = None
            data = archive_file.read(data_len)

            try:
                if encrypted:
                    data = fernet.decrypt(data)
                files_to_extract.append((filename, data, crc32_expected))
                file_count += 1
            except InvalidToken as exc:
                raise InvalidArchivePasswordError(
                    "Incorrect password or damaged ADC archive."
                ) from exc

        os.makedirs(dest_dir, exist_ok=True)
        with Bar("Extracting files...", max=file_count) as bar:
            for filename, compressed_data, crc32_expected in files_to_extract:
                decompressed_data = parma_decompress(compressed_data)
                if decompressed_data is not None:
                    if crc32_expected is not None:
                        calculated_crc32 = zlib.crc32(decompressed_data) & 0xFFFFFFFF
                        if calculated_crc32 != crc32_expected:
                            print(f"CRC32 integrity check failed for {filename}: expected {crc32_expected:08x}, got {calculated_crc32:08x}")
                    output_path = os.path.join(dest_dir, filename)
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    with open(output_path, "wb") as output_file:
                        output_file.write(decompressed_data)
                else:
                    print(f"Error decompressing {filename}")
                bar.next()
        print(f"ADC archive extracted to {dest_dir}")
