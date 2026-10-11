import os
import zlib

from libadc.archive import (
    create_adc_archive,
    extract_adc_archive,
    _list_files_in_path,
)
from adc.headless import run_headless_flow
from libadc.compression import read_binary_file, parma_compress

def test_create_and_extract(tmp_path, monkeypatch):
    file_path = tmp_path / "hello.txt"
    file_path.write_bytes(b"Hello ADC!")

    archive_path = tmp_path / "test.adc"

    monkeypatch.setattr("builtins.input", lambda _: "n")

    create_adc_archive([str(file_path)], str(archive_path), format="adc")
    assert archive_path.exists()

    output_dir = tmp_path / "extract"
    output_dir.mkdir()
    extract_adc_archive(str(archive_path), str(output_dir))

    extracted_file = output_dir.joinpath("test").joinpath("hello.txt")
    assert extracted_file.read_bytes() == b"Hello ADC!"


def test_wrong_adc_password_reports_error_without_creating_output_dir(
    tmp_path, monkeypatch, capsys
):
    file_path = tmp_path / "secret.txt"
    file_path.write_bytes(b"Secret content")

    archive_path = tmp_path / "protected.adc"
    create_adc_archive(
        [str(file_path)],
        str(archive_path),
        format="adc",
        password="test-password",
    )
    monkeypatch.setattr("libadc.archive.getpass.getpass", lambda _: "wrong-password")

    output_dir = tmp_path / "extract"
    run_headless_flow(["adc", "e", str(archive_path), str(output_dir)])

    assert "Error: Incorrect password or damaged ADC archive." in capsys.readouterr().out
    assert not output_dir.exists()


def test_read_binary_file_refreshes_after_write(tmp_path):
    file_path = tmp_path / "data.bin"
    file_path.write_bytes(b"first")

    first_bytes = read_binary_file(str(file_path))
    assert first_bytes == b"first"

    file_path.write_bytes(b"second")
    os.utime(str(file_path), None)

    second_bytes = read_binary_file(str(file_path))
    assert second_bytes == b"second"
    assert first_bytes != second_bytes


def test_create_and_extract_zip_with_password(tmp_path):
    file_path = tmp_path / "hello.txt"
    file_path.write_bytes(b"Hello ZIP with password!")

    archive_path = tmp_path / "test.zip"
    create_adc_archive([str(file_path)], str(archive_path), format="zip", password="secret")
    assert archive_path.exists()

    output_dir = tmp_path / "extract"
    output_dir.mkdir()
    extract_adc_archive(str(archive_path), str(output_dir), password="secret")

    extracted_file = output_dir.joinpath("test").joinpath("hello.txt")
    assert extracted_file.read_bytes() == b"Hello ZIP with password!"


def test_extract_legacy_1_2_0_format(tmp_path):
    """Test backwards compatibility with ADC 1.2.0 format (no header, 4-byte data length)"""
    # Create a legacy 1.2.0 format archive manually
    legacy_archive = tmp_path / "legacy.adc"
    
    # File 1
    filename1 = "test1.txt"
    content1 = b"Hello from legacy format!"
    compressed1 = parma_compress(content1)
    
    # File 2
    filename2 = "test2.txt"
    content2 = b"Another file in legacy format"
    compressed2 = parma_compress(content2)
    
    # Write legacy format: [filename_len (2 bytes)][filename][data_len (4 bytes)][data]...
    with open(legacy_archive, "wb") as f:
        # Write first file
        f.write(len(filename1).to_bytes(2, "big"))
        f.write(filename1.encode("utf-8"))
        f.write(len(compressed1).to_bytes(4, "big"))  # 4 bytes for legacy format
        f.write(compressed1)
        
        # Write second file
        f.write(len(filename2).to_bytes(2, "big"))
        f.write(filename2.encode("utf-8"))
        f.write(len(compressed2).to_bytes(4, "big"))  # 4 bytes for legacy format
        f.write(compressed2)
    
    # Extract the legacy archive using current code
    output_dir = tmp_path / "extract"
    output_dir.mkdir()
    extract_adc_archive(str(legacy_archive), str(output_dir))
    
    # Verify extraction
    extracted_file1 = output_dir.joinpath("legacy").joinpath("test1.txt")
    extracted_file2 = output_dir.joinpath("legacy").joinpath("test2.txt")
    
    assert extracted_file1.exists()
    assert extracted_file2.exists()
    assert extracted_file1.read_bytes() == content1
    assert extracted_file2.read_bytes() == content2
