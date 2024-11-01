import os
import zlib
import tkinter as tk
from tkinter import filedialog

def read_binary_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def parma_compress(data):
    return zlib.compress(data)

def parma_decompress(compressed_data):
    return zlib.decompress(compressed_data)

def create_adc_archive(file_paths, output_path):
    with open(output_path, 'wb') as archive_file:
        for file_path in file_paths:
            filename = os.path.basename(file_path).encode('utf-8')
            original_data = read_binary_file(file_path)
            compressed_data = parma_compress(original_data)
            archive_file.write(len(filename).to_bytes(2, 'big'))
            archive_file.write(filename)
            archive_file.write(len(compressed_data).to_bytes(4, 'big'))
            archive_file.write(compressed_data)
    print(f"Archive created: {output_path}")

def extract_adc_archive(archive_path, output_dir):
    with open(archive_path, 'rb') as archive_file:
        while True:
            filename_len_bytes = archive_file.read(2)
            if not filename_len_bytes:
                break
            filename_len = int.from_bytes(filename_len_bytes, 'big')
            filename = archive_file.read(filename_len).decode('utf-8')
            compressed_data_len_bytes = archive_file.read(4)
            compressed_data_len = int.from_bytes(compressed_data_len_bytes, 'big')
            compressed_data = archive_file.read(compressed_data_len)
            decompressed_data = parma_decompress(compressed_data)
            output_path = os.path.join(output_dir, filename)
            with open(output_path, 'wb') as output_file:
                output_file.write(decompressed_data)
            print(f"Extracted: {output_path}")

def select_files_for_archiving():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    files = filedialog.askopenfilenames(title="Select files to archive")
    return list(files)

def select_directory_for_extraction():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    folder = filedialog.askdirectory(title="Select directory to extract files to")
    return folder

def save_archive_file():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    file_path = filedialog.asksaveasfilename(defaultextension=".adc", title="Save archive as")
    return file_path

def open_archive_file():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    file_path = filedialog.askopenfilename(filetypes=[("ADC files", "*.adc")], title="Select ADC archive to extract")
    return file_path

def main():
    if len(os.sys.argv) > 1:
        archive_to_extract = os.sys.argv[1]
        if archive_to_extract.endswith('.adc'):
            extraction_directory = select_directory_for_extraction()
            if extraction_directory:
                extract_adc_archive(archive_to_extract, extraction_directory)
            else:
                print("No output directory specified. Aborting.")
        else:
            print("Invalid file type. Please provide a valid ADC archive.")
        input("Press any key to close...")
        return

    print("Welcome to the ADC Archiver!")
    print("Type 'c' to create an archive or 'e' to extract an archive.")
    command = input("Enter your choice: ").strip().lower()

    if command == 'c':
        files_to_archive = select_files_for_archiving()
        if files_to_archive:
            output_archive = save_archive_file()
            if output_archive:
                create_adc_archive(files_to_archive, output_archive)
            else:
                print("No output file specified. Aborting.")
        else:
            print("No files selected. Aborting.")
    elif command == 'e':
        archive_to_extract = open_archive_file()
        if archive_to_extract:
            extraction_directory = select_directory_for_extraction()
            if extraction_directory:
                extract_adc_archive(archive_to_extract, extraction_directory)
            else:
                print("No output directory specified. Aborting.")
        else:
            print("No archive selected. Aborting.")
    else:
        print("Invalid command. Please type 'c' to create an archive or 'e' to extract one.")
    input("Press any key to close...")

if __name__ == "__main__":
    main()