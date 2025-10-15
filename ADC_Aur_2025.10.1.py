# This is a live development version of ADC Archiver.
# It is not recommended and meant for use in this state.
# If you want to use ADC Archiver stable, You can find the stable version on the GitHub page.
# ADC Canary may not work!

# ADC Archiver Aurora
# Version: 2025.10.1
# byte-key: 8
# GitHub page: https://github.com/Mealman1551/ADC
# Webpage: https://mealman1551.github.io/adc.html
# Webpage 2: https://mealman1551.github.io/ADC.html

# This source code was made in Python 3.12.11 and Python 3.12.x is required to compile.

# (c) 2025 Mealman1551

import os
import zlib
import tkinter as tk
from tkinter import filedialog
import socket
from progress.bar import Bar
from colorama import init
import getpass
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import base64
import zipfile
import tarfile

init(autoreset=True)

RED = "\033[31m"
GREEN = "\033[32m"
PURPLE = "\033[35m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
ORANGE = "\033[38;5;208m"
TEAL = "\033[38;5;37m"
WHITE = "\033[37m"
GRAY = "\033[90m"
LIGHT_BLUE = "\033[94m"
LIGHT_GREEN = "\033[92m"
LIGHT_RED = "\033[91m"
LIGHT_PURPLE = "\033[95m"
LIGHT_CYAN = "\033[96m"
LIGHT_YELLOW = "\033[93m"
LIGHT_ORANGE = "\033[38;5;214m"
LIGHT_GRAY = "\033[90m"
LIGHT_TEAL = "\033[38;5;123m"
LIGHT_MAGENTA = "\033[95m"
BLINK = "\033[5m"
UNDERLINE = "\033[4m"
REVERSE = "\033[7m"
BLACK = "\033[30m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
reset = "\033[0m"


def run():
    main()


dev = socket.gethostname()
name = getpass.getuser()
opr = os.sys.platform

if opr in ["linux", "posix"]:
    print(
        rf"""
    _    ____   ____      _             _     _                
   / \  |  _ \ / ___|    / \   _ __ ___| |__ (_)_   _____ _ __ 
  / _ \ | | | | |       / _ \ | '__/ __| '_ \| \ \ / / _ \ '__|
 / ___ \| |_| | |___   / ___ \| | | (__| | | | |\ V /  __/ |   
/_/   \_\____/ \____| /_/   \_\_|  \___|_| |_|_| \_/ \___|_|   
                                                               
  __              _     _                  
 / _| ___  _ __  | |   (_)_ __  _   ___  __
| |_ / _ \| '__| | |   | | '_ \| | | \ \/ /
|  _| (_) | |    | |___| | | | | |_| |>  < 
|_|  \___/|_|    |_____|_|_| |_|\__,_/_/\_\
        
    """
    )


def derive_key_from_password(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))


def read_binary_file(file_path):
    with open(file_path, "rb") as file:
        return file.read()


def parma_compress(data):
    return zlib.compress(data)


def parma_decompress(compressed_data):
    try:
        return zlib.decompress(compressed_data)
    except zlib.error as e:
        print(f"Decompress error: {e}")
        return None


def create_adc_archive(file_paths, output_path, format="adc"):
    if format.startswith("tar"):
        mode = "w"
        if output_path.endswith(".tar.gz"):
            mode = "w:gz"
        elif output_path.endswith(".tar.xz"):
            mode = "w:xz"
        elif output_path.endswith(".tar.bz2"):
            mode = "w:bz2"

        with tarfile.open(output_path, mode) as tar:
            with Bar("Compressing files...", max=len(file_paths)) as bar:
                for file_path in file_paths:
                    tar.add(file_path, arcname=os.path.basename(file_path))
                    bar.next()
        print(f"TAR archive created: {output_path}")
        return

    if format == "zip":
        with zipfile.ZipFile(output_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            with Bar("Compressing files...", max=len(file_paths)) as bar:
                for file_path in file_paths:
                    zf.write(file_path, arcname=os.path.basename(file_path))
                    bar.next()
        print(f"ZIP archive created: {output_path}")
        return

    use_password = (
        input("Do you want to protect this archive with a password? (y/n): ")
        .strip()
        .lower()
        == "y"
    )
    if use_password:
        pwd = getpass.getpass("Create a password for this archive: ")
        salt = os.urandom(16)
        key = derive_key_from_password(pwd, salt)
        fernet = Fernet(key)

    with open(output_path, "wb") as archive_file:
        if use_password:
            archive_file.write(b"ADCARCH\x00")
            archive_file.write(salt)

        with Bar("Compressing files...", max=len(file_paths)) as bar:
            for file_path in file_paths:
                filename = os.path.basename(file_path).encode("utf-8")
                original_data = read_binary_file(file_path)
                compressed_data = parma_compress(original_data)

                if use_password:
                    data_to_write = fernet.encrypt(compressed_data)
                else:
                    data_to_write = compressed_data

                archive_file.write(len(filename).to_bytes(2, "big"))
                archive_file.write(filename)
                archive_file.write(len(data_to_write).to_bytes(8, "big"))
                archive_file.write(data_to_write)
                bar.next()
    print(f"ADC archive created: {output_path}")


def extract_adc_archive(archive_path, output_dir, format=None):
    if not format:
        if archive_path.lower().endswith((".tar", ".tar.gz", ".tar.xz", ".tar.bz2")):
            format = "tar"
        elif archive_path.lower().endswith(".zip"):
            format = "zip"
        else:
            format = "adc"

    if format == "tar":
        with tarfile.open(archive_path, "r:*") as tar:
            members = tar.getmembers()
            with Bar("Extracting files...", max=len(members)) as bar:
                for member in members:
                    tar.extract(member, path=output_dir)
                    bar.next()
        print(f"TAR archive extracted to: {output_dir}")
        return

    if format == "zip":
        with zipfile.ZipFile(archive_path, "r") as zf:
            file_list = zf.namelist()
            with Bar("Extracting files...", max=len(file_list)) as bar:
                for f in file_list:
                    zf.extract(f, path=output_dir)
                    bar.next()
        print(f"ZIP archive extracted to: {output_dir}")
        return

    with open(archive_path, "rb") as archive_file:
        header = archive_file.read(8)
        if header == b"ADCARCH\x00":
            salt = archive_file.read(16)
            pwd = getpass.getpass("Enter password for archive: ")
            key = derive_key_from_password(pwd, salt)
            fernet = Fernet(key)
            encrypted = True
        else:
            archive_file.seek(0)
            encrypted = False

        file_count = 0
        files_to_extract = []

        while True:
            filename_len_bytes = archive_file.read(2)
            if not filename_len_bytes:
                break
            filename_len = int.from_bytes(filename_len_bytes, "big")
            filename = archive_file.read(filename_len).decode("utf-8", errors="ignore")
            data_len_bytes = archive_file.read(8)
            data_len = int.from_bytes(data_len_bytes, "big")
            data = archive_file.read(data_len)

            try:
                if encrypted:
                    data = fernet.decrypt(data)
                files_to_extract.append((filename, data))
                file_count += 1
            except Exception as e:
                print(f"Error decrypting {filename}: {e}")
                continue

        with Bar("Extracting files...", max=file_count) as bar:
            for filename, compressed_data in files_to_extract:
                decompressed_data = parma_decompress(compressed_data)
                if decompressed_data is not None:
                    output_path = os.path.join(output_dir, filename)
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    with open(output_path, "wb") as output_file:
                        output_file.write(decompressed_data)
                else:
                    print(f"Error decompressing {filename}")
                bar.next()
        print(f"ADC archive extracted to {output_dir}")


def select_files_for_archiving():
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    files = filedialog.askopenfilenames(title="Select files to archive")
    root.destroy()
    return list(files)


def select_directory_for_extraction():
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    folder = filedialog.askdirectory(title="Select directory to extract files to")
    root.destroy()
    return folder


def save_archive_file(format="adc"):
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    extensions = {
        "adc": (".adc", [("ADC archives", "*.adc")]),
        "zip": (".zip", [("ZIP archives", "*.zip")]),
        "tar": (".tar", [("TAR archives", "*.tar")]),
        "tar.gz": (".tar.gz", [("TAR.GZ archives", "*.tar.gz")]),
        "tar.xz": (".tar.xz", [("TAR.XZ archives", "*.tar.xz")]),
        "tar.bz2": (".tar.bz2", [("TAR.BZ2 archives", "*.tar.bz2")]),
    }

    default_ext, filetypes = extensions.get(
        format, (".adc", [("ADC archives", "*.adc")])
    )
    file_path = filedialog.asksaveasfilename(
        defaultextension=default_ext,
        filetypes=filetypes,
        title="Save archive as",
    )
    root.destroy()
    return file_path


def open_archive_file():
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    filetypes = [
        ("ADC archives", "*.adc"),
        ("ZIP archives", "*.zip"),
        ("TAR archives", "*.tar"),
        ("TAR.GZ archives", "*.tar.gz"),
        ("TAR.XZ archives", "*.tar.xz"),
        ("TAR.BZ2 archives", "*.tar.bz2"),
        ("All files", "*.*"),
    ]

    file_path = filedialog.askopenfilename(
        filetypes=filetypes,
        title="Select archive to extract",
    )
    root.destroy()
    return file_path


def main():
    print(
        #f"""
         # You are using ADC canary, this code is not stable and may not work!
          #If you are using this on accident quit by pressing 'Q' or 'q'.
                       
           # You can download the stable version of ADC Archiver on GitHub:
            #{PURPLE}https://github.com/Mealman1551/ADC{reset}
          #"""
    )

    if len(os.sys.argv) > 1:
        subcommand = os.sys.argv[1]
        if subcommand == "c":
            if len(os.sys.argv) < 4:
                print("Use: adc.exe or adc.bin c <files...> <output.adc>")
                return
            files = os.sys.argv[2:-1]
            output = os.sys.argv[-1]
            create_adc_archive(files, output)
            return
        elif subcommand == "e":
            if len(os.sys.argv) < 3:
                print("Use: adc.exe or adc.bin e <archive.adc> [output_folder]")
                return
            archive = os.sys.argv[2]
            folder = os.sys.argv[3] if len(os.sys.argv) >= 4 else os.getcwd()
            extract_adc_archive(archive, folder)
            return
        else:
            print("Unknown command.")
            print(
                "Use:\n  adc.exe or adc.bin c <files...> <output.adc>\n  adc.exe or adc.bin e <archive.adc> [output_folder]"
            )
            return

    while True:
        command = (
            input(
                f"Welcome to the ADC Archiver {YELLOW}Canary{reset}! Enter command ('c' to create, 'e' to extract, 'i' for info, 'q' to quit): "
            )
            .strip()
            .lower()
        )

        if command in ("c", "create"):
            files_to_archive = select_files_for_archiving()
            if files_to_archive:
                fmt = input(
                    "Choose format: [1] ADC (default), [2] ZIP, [3] TAR, [4] TAR.GZ, [5] TAR.XZ, [6] TAR.BZ2]: "
                ).strip()
                if fmt == "2":
                    fmt = "zip"
                elif fmt == "3":
                    fmt = "tar"
                elif fmt == "4":
                    fmt = "tar.gz"
                elif fmt == "5":
                    fmt = "tar.xz"
                elif fmt == "6":
                    fmt = "tar.bz2"
                else:
                    fmt = "adc"

                output_archive = save_archive_file(format=fmt)
                if output_archive:
                    create_adc_archive(files_to_archive, output_archive, format=fmt)
                else:
                    print("No output file specified. Aborting.")
            else:
                print("No files selected. Aborting.")

        elif command in ("e", "extract"):
            archive_to_extract = open_archive_file()
            if archive_to_extract:
                extraction_directory = select_directory_for_extraction()
                if extraction_directory:
                    extract_adc_archive(archive_to_extract, extraction_directory)
                else:
                    print("No output directory specified. Aborting.")
            else:
                print("No archive selected. Aborting.")

        elif command == "i":
            info = f"""
             {RED}####{reset}        {PURPLE}%%%%%%%%%%%{reset}         {GREEN}********{reset}  
            {RED}######{reset}       {PURPLE}%%%%%%%%%%%{reset}      {GREEN}*************{reset}
           {RED}### ###{reset}      {PURPLE}%%%%      %%%%{reset}   {GREEN}****      ****{reset}
          {RED}###  ###{reset}      {PURPLE}%%%       %%%%{reset}  {GREEN}****           {reset}
         {RED}###   ####{reset}     {PURPLE}%%%       %%%%{reset}  {GREEN}***            {reset}
        {RED}###    ####{reset}     {PURPLE}%%%      %%%%{reset}   {GREEN}****            {reset}
       {RED}#############{reset}    {PURPLE}%%%      %%%%{reset}   {GREEN}****       ***{reset}  
      {RED}####       ###{reset}   {PURPLE}%%%%%%%%%%%%{reset}      {GREEN}************{reset}   
     {RED}####        ####{reset}  {PURPLE}%%%%%%%%%{reset}          {GREEN}*******{reset}  

        | ADC Archiver {TEAL}Aurora{reset} | Version: 2025.10.1 |

        
        GitHub page: https://github.com/Mealman1551/ADC
        Webpage: https://mealman1551.github.io/adc.html
        Webpage 2: https://mealman1551.github.io/ADC
        E-mail: adc@linuxmail.org

        ---------

        You are hosting ADC on: {ORANGE}{dev}{reset}
        You are using ADC as: {ORANGE}{name}{reset}
        You are using ADC on: {ORANGE}{opr}{reset}

        (c) 2025 Mealman1551
        """
            print(info)

        elif command in ("q", "exit", "quit"):
            print(f"Thank you for using ADC Archiver {TEAL}Aurora{reset}!")
            break

        else:
            print(
                "Invalid command. Please type 'c' to create, 'e' to extract, 'i' for info or 'q' to quit."
            )


run()
