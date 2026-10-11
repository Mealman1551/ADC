# ADC Archiver - main module
# (c) 2026 Mealman1551

import os
import sys
import socket
import getpass
import platform
from colorama import init

from libadc.constants import YELLOW, PURPLE, GREEN, reset, VERSION
from .updater import check_and_show_update
from .ascii_art import print_banner, get_info_banner
from libadc.archive import (
    InvalidArchivePasswordError,
    create_adc_archive,
    extract_adc_archive,
)
from .ui import (
    select_files_for_archiving,
    select_directory_for_extraction,
    save_archive_file,
    open_archive_file,
)


def has_display():
    # On Windows, always assume display is available
    if platform.system().lower() == "windows":
        return True
    # On Linux/Unix, check for DISPLAY or WAYLAND_DISPLAY
    return bool(os.environ.get("DISPLAY") or os.environ.get("WAYLAND_DISPLAY"))


init(autoreset=True)


dev = socket.gethostname()
name = getpass.getuser()
opr = platform.system().lower()


def run():
    main()


def main():
    headless_flag = "--headless" in sys.argv

    adc_file_arg = None
    if len(sys.argv) == 2 and not sys.argv[1].startswith("--"):
        arg = sys.argv[1]
        if os.path.isfile(arg) and arg.lower().endswith(".adc"):
            adc_file_arg = arg

    if adc_file_arg:
        output_dir = os.path.dirname(os.path.abspath(adc_file_arg))
        print(f"{YELLOW}Auto-extracting {adc_file_arg} to {output_dir}{reset}")
        try:
            extract_adc_archive(adc_file_arg, output_dir)
        except InvalidArchivePasswordError as exc:
            print(f"Error: {exc}")
        return

    has_cli_args = len([arg for arg in sys.argv[1:] if arg != "--headless"]) > 0

    if headless_flag or not has_display() or has_cli_args:
        from .headless import run_headless_flow

        filtered_args = [arg for arg in sys.argv if arg != "--headless"]
        run_headless_flow(filtered_args)
    else:
        run_interactive()


def run_interactive():
    print_banner()


    print(
        f"""
You are using ADC {VERSION}, this code is not stable and may not work!
If you are using this on accident quit by pressing 'q'.

You can download the stable version of ADC Archiver on GitHub releases:
{PURPLE}https://github.com/Mealman1551/ArchivedDataCodec/releases/latest{reset}
        """
    )

    while True:
        command = (
            input(
                f"Welcome to ADC Archiver {VERSION} | Enter command ('c' to create, 'e' to extract, 'i' for info, 'q' to quit): "
            )
            .strip()
            .lower()
        )

        if command in ("c", "create"):
            files = select_files_for_archiving()
            if not files:
                print("No files selected. Aborting.")
                continue

            fmt = input(
                "Choose format: [1] ADC (default), [2] ZIP, [3] TAR, [4] TAR.GZ, [5] TAR.XZ, [6] TAR.BZ2, [7] 7Z]: "
            ).strip()
            fmt_map = {
                "2": "zip",
                "3": "tar",
                "4": "tar.gz",
                "5": "tar.xz",
                "6": "tar.bz2",
                "7": "7z",
            }
            fmt = fmt_map.get(fmt, "adc")

            output_archive = save_archive_file(format=fmt)
            if output_archive:
                password = None
                if fmt in ("adc", "zip"):
                    use_password = input("Do you want to protect this archive with a password? (y/n): ").strip().lower() == "y"
                    if use_password:
                        password = getpass.getpass("Create a password for this archive: ")
                
                create_adc_archive(files, output_archive, format=fmt, password=password)
                print(f"\n[INFO] Archive created: {output_archive}\n")
            else:
                print("No output file specified. Aborting.")

        elif command in ("e", "extract"):
            archive = open_archive_file()
            if not archive:
                print("No archive selected. Aborting.")
                continue

            extraction_dir = select_directory_for_extraction() or "."
            try:
                extract_adc_archive(archive, extraction_dir)
            except InvalidArchivePasswordError as exc:
                print(f"Error: {exc}")
                continue
            print(f"\n[INFO] Archive extracted to: {extraction_dir}\n")

        elif command == "i":
            info = get_info_banner(dev, name, opr)
            print(info)

        elif command in (
            "q",
            "quit",
            "exit",
            "stop",
            "bye",
            "goodbye",
            "end",
            "close",
            "terminate",
            "shutdown",
            "leave",
            "byebye",
        ):
            print(f"Thank you for using ADC Archiver {VERSION}!")
            break

        else:
            print("Invalid command. Please type 'c', 'e', 'i' or 'q'.")


if __name__ == "__main__":
    run()
