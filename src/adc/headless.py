# ADC Archiver - Headless Module
# (c) 2026 Mealman1551


import os
import shlex
import getpass
from pathlib import Path
from libadc.archive import (
    InvalidArchivePasswordError,
    create_adc_archive,
    extract_adc_archive,
)


def parse_path_input(value):
    if not value:
        return None

    # Strip outer quotes if present
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        value = value[1:-1]

    # Expand user (~) and resolve to absolute path
    return str(Path(value).expanduser().resolve())


def parse_paths_input(value):
    if not value:
        return []

    try:
        # Use shlex to properly handle quoted strings
        paths = shlex.split(value)
    except ValueError:
        # If shlex fails (unmatched quotes), fall back to simple split
        paths = value.split()

    result = []
    for p in paths:
        expanded = parse_path_input(p)
        if expanded and os.path.exists(expanded):
            result.append(expanded)
        else:
            print(f"Path does not exist: {p}")

    return result


def prompt_for_files_to_archive():
    print("Enter files or directories to archive (use quotes for paths with spaces)")
    value = input("Paths: ").strip()
    return parse_paths_input(value)


def prompt_for_output_archive_format():
    value = (
        input("Format (adc, zip, tar, tar.gz, tar.xz, tar.bz2, 7z) [adc]: ")
        .strip()
        .lower()
    )
    if value not in [
        "adc",
        "zip",
        "tar",
        "tar.gz",
        "tar.xz",
        "tar.bz2",
        "7z",
    ]:
        value = "adc"
    return value


def prompt_for_output_archive_path(fmt):
    default = f"archive.{fmt}"
    value = input(f"Output archive path [{default}]: ").strip()

    if not value:
        return default

    # Parse the path to handle quotes and expansion
    parsed = parse_path_input(value)

    # If it's a directory, append the default filename
    if os.path.isdir(parsed):
        return str(Path(parsed) / default)

    return parsed


def prompt_for_archive_to_extract():
    value = input("Path to archive: ").strip()
    return parse_path_input(value) if value else None


def prompt_for_extraction_output_dir():
    value = input("Extraction directory [.]: ").strip()
    parsed = parse_path_input(value if value else ".")

    return parsed


def prompt_for_password_if_needed(fmt):
    """Prompt for password if creating an ADC or ZIP archive."""
    if fmt not in ("adc", "zip"):
        return None

    use_password = input("Do you want to protect this archive with a password? (y/n): ").strip().lower() == "y"
    if use_password:
        return getpass.getpass("Create a password for this archive: ")
    return None


def run_headless_flow(argv):
    if len(argv) < 2:
        print("Usage: adc c <paths> or adc e <archive> [output]")
        return

    command = argv[1].lower()

    if command in ("c", "create"):
        # Get files from command line args or prompt
        files = []
        if len(argv) > 2:
            # Parse command line paths
            for path_arg in argv[2:]:
                expanded = parse_path_input(path_arg)
                if expanded and os.path.exists(expanded):
                    files.append(expanded)
                else:
                    print(f"Path does not exist: {path_arg}")

        if not files:
            files = prompt_for_files_to_archive()
            if not files:
                print("No valid files selected. Aborting.")
                return

        fmt = prompt_for_output_archive_format()
        output = prompt_for_output_archive_path(fmt)
        
        password = prompt_for_password_if_needed(fmt)
        
        create_adc_archive(files, output, format=fmt, password=password)
        print(f"Archive created: {output}")

    elif command in ("e", "extract"):
        archive_path = None
        if len(argv) > 2:
            archive_path = parse_path_input(argv[2])
        else:
            archive_path = prompt_for_archive_to_extract()

        if not archive_path or not os.path.exists(archive_path):
            print(f"Archive not found: {archive_path}")
            return

        output_dir = None
        if len(argv) > 3:
            output_dir = parse_path_input(argv[3])
        else:
            output_dir = prompt_for_extraction_output_dir()

        try:
            extract_adc_archive(archive_path, output_dir)
        except InvalidArchivePasswordError as exc:
            print(f"Error: {exc}")
            return
        print(f"Archive extracted to: {output_dir}")

    else:
        print("Unknown command")
