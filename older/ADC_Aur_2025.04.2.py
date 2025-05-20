import os
import zlib
import tkinter as tk
from tkinter import filedialog
import socket
from time import sleep
from progress.bar import Bar
from colorama import init

init(autoreset=True)

RED = "\033[31m"
GREEN = "\033[32m"
PURPLE = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

device_name = socket.gethostname()
user_name = os.getlogin()

def read_binary_file(file_path):
    """Read the contents of a file in binary mode."""
    with open(file_path, 'rb') as file:
        return file.read()

def compress_data(data):
    """Compress data using zlib."""
    return zlib.compress(data)

def decompress_data(compressed_data):
    """Decompress data using zlib."""
    try:
        return zlib.decompress(compressed_data)
    except zlib.error as e:
        print(f"Decompression error: {e}")
        return None

def create_adc_archive(file_paths, output_path):
    """Create an ADC archive from the given files."""
    with open(output_path, 'wb') as archive_file:
        with Bar('Compressing files...', max=len(file_paths)) as progress_bar:
            for file_path in file_paths:
                # Get the file name and read its contents
                file_name = os.path.basename(file_path).encode('utf-8')
                original_data = read_binary_file(file_path)
                compressed_data = compress_data(original_data)

                archive_file.write(len(file_name).to_bytes(2, 'big'))
                archive_file.write(file_name)
                archive_file.write(len(compressed_data).to_bytes(8, 'big'))
                archive_file.write(compressed_data)

                progress_bar.next()
    print(f"Archive created: {output_path}")

def extract_adc_archive(archive_path, output_dir):
    """Extract files from an ADC archive."""
    with open(archive_path, 'rb') as archive_file:
        files_to_extract = []

        while True:
            file_name_length_bytes = archive_file.read(2)
            if not file_name_length_bytes:
                break

            file_name_length = int.from_bytes(file_name_length_bytes, 'big')
            file_name = archive_file.read(file_name_length).decode('utf-8', errors='ignore')

            compressed_data_length_bytes = archive_file.read(8)
            compressed_data_length = int.from_bytes(compressed_data_length_bytes, 'big')
            compressed_data = archive_file.read(compressed_data_length)

            files_to_extract.append((file_name, compressed_data))

        with Bar('Extracting files...', max=len(files_to_extract)) as progress_bar:
            for file_name, compressed_data in files_to_extract:
                decompressed_data = decompress_data(compressed_data)
                if decompressed_data is not None:
                    output_path = os.path.join(output_dir, file_name)
                    with open(output_path, 'wb') as output_file:
                        output_file.write(decompressed_data)
                else:
                    print(f"Skipping extraction for {file_name} due to decompression error.")
                progress_bar.next()
    print(f"Extraction complete to {output_dir}")

def select_files_for_archiving():
    """Open a file dialog to select files for archiving."""
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    files = filedialog.askopenfilenames(title="Select files to archive")
    root.destroy()
    return list(files)

def select_directory_for_extraction():
    """Open a file dialog to select a directory for extraction."""
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    folder = filedialog.askdirectory(title="Select directory to extract files to")
    root.destroy()
    return folder

def save_archive_file():
    """Open a file dialog to specify the output archive file."""
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    file_path = filedialog.asksaveasfilename(defaultextension=".adc", title="Save ADC archive as")
    root.destroy()
    return file_path

def open_archive_file():
    """Open a file dialog to select an archive file for extraction."""
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    file_path = filedialog.askopenfilename(filetypes=[("ADC archives", "*.adc")], title="Select ADC archive to extract")
    root.destroy()
    return file_path

def main():
    """Main function to handle command-line arguments."""
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

while True:
    command = input("Welcome to the ADC Archiver! Enter command (c to create, e to extract, i for info, q to quit): ").strip().lower()
    
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

    elif command == 'i':
        info = r"""

             {0}####{1}        {2}%%%%%%%%%%%{1}         {3}********{1}  
            {0}######{1}       {2}%%%%%%%%%%%{1}     {3} *************{1}
           {0}### ###{1}      {2}%%%%      %%%%{1}   {3}****      ****{1}
          {0}###  ###{1}      {2}%%%       %%%%{1}  {3}****           {1}
         {0}###   ####{1}     {2}%%%       %%%%{1}  {3}***            {1}
        {0}###    ####{1}    {2}%%%%      %%%%{1}  {3}****            {1}
      {0}#############{1}    {2}%%%      %%%%{1}   {3}****       ***{1}  
     {0}####       ###{1}   {2}%%%%%%%%%%%%{1}     {3} ************   {1}   
    {0}####        ####{1}  {2}%%%%%%%%%{1}          {3}*******      {1}  

    | ADC Archiver {4}Aurora{1} | Version 2025.04.2 | byte-key: 8 |
    
    GitHub page: https://github.com/Mealman1551/ADC
    Webpage: https://mealman1551.github.io/adc.html
    Webpage 2: https://mealman1551.github.io/ADC
    e-mail: adc@linuxmail.org
    (c) 2025 Mealman1551   
    
""".format(RED, RESET, PURPLE, GREEN, CYAN)
        
        print(info)
    
    elif command == 'q':
        print("Thank you for using ADC Archiver Aurora!")
        break

    else:
        print("Invalid command. Please type 'c' to create, 'e' to extract, 'i' for info or 'q' to quit.")
