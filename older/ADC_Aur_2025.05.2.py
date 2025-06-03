import os
import zlib
import tkinter as tk
from tkinter import filedialog
import socket
from time import sleep
from progress.bar import Bar
from colorama import init
import getpass


init(autoreset=True)

RED = "\033[31m"
GREEN = "\033[32m"
PURPLE = "\033[35m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
reset = "\033[0m"

dev = socket.gethostname()
name = getpass.getuser()


opr = os.sys.platform

if opr == 'linux' or opr == 'posix':
    print(f"""{BLUE}
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
        
    {reset}""")

def read_binary_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def parma_compress(data):
    return zlib.compress(data)

def parma_decompress(compressed_data):
    try:
        return zlib.decompress(compressed_data)
    except zlib.error as e:
        print(f"Decompres error: {e}")
        return None

def create_adc_archive(file_paths, output_path):
    with open(output_path, 'wb') as archive_file:
        with Bar('Compressing files...', max=len(file_paths)) as bar:
            for file_path in file_paths:
                filename = os.path.basename(file_path).encode('utf-8')
                original_data = read_binary_file(file_path)
                compressed_data = parma_compress(original_data)

                archive_file.write(len(filename).to_bytes(2, 'big'))
                archive_file.write(filename)
                archive_file.write(len(compressed_data).to_bytes(8, 'big'))
                archive_file.write(compressed_data)
                bar.next()
    print(f"Archive created: {output_path}")

def extract_adc_archive(archive_path, output_dir):
    with open(archive_path, 'rb') as archive_file:
        file_count = 0
        files_to_extract = []
        
        while True:
            filename_len_bytes = archive_file.read(2)
            if not filename_len_bytes:
                break
            filename_len = int.from_bytes(filename_len_bytes, 'big')
            filename = archive_file.read(filename_len)
            try:
                filename = filename.decode('utf-8')
            except UnicodeDecodeError:
                filename = filename.decode('windows-1252', errors='ignore')

            compressed_data_len_bytes = archive_file.read(8)
            compressed_data_len = int.from_bytes(compressed_data_len_bytes, 'big')
            compressed_data = archive_file.read(compressed_data_len)
            files_to_extract.append((filename, compressed_data))
            file_count += 1

        with Bar('Extracting files...', max=file_count) as bar:
            for filename, compressed_data in files_to_extract:
                decompressed_data = parma_decompress(compressed_data)
                if decompressed_data is not None:
                    output_path = os.path.join(output_dir, filename)
                    with open(output_path, 'wb') as output_file:
                        output_file.write(decompressed_data)
                    bar.next()
                else:
                    print(f"Skipping extraction for {filename} due to decompression error.")
            print(f"Extraction complete to {output_dir}")

def select_files_for_archiving():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    files = filedialog.askopenfilenames(title="Select files to archive")
    root.destroy()
    return list(files)

def select_directory_for_extraction():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    folder = filedialog.askdirectory(title="Select directory to extract files to")
    root.destroy()
    return folder

def save_archive_file():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    file_path = filedialog.asksaveasfilename(defaultextension=".adc", title="Save ADC archive as")
    root.destroy()
    return file_path

def open_archive_file():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    file_path = filedialog.askopenfilename(filetypes=[("ADC archives", "*.adc")], title="Select ADC archive to extract")
    root.destroy()
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

while True:
    command = input(f"Welcome to the ADC Archiver {CYAN}Aurora{reset}! Enter command ('c' to create, 'e' to extract, 'i' for info, 'q' to quit): ").strip().lower()
    
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

        info = f"""

             {RED}####{reset}        {PURPLE}%%%%%%%%%%%{reset}         {GREEN}********{reset}  
            {RED}######{reset}       {PURPLE}%%%%%%%%%%%{reset}     {GREEN} *************{reset}
           {RED}### ###{reset}      {PURPLE}%%%%      %%%%{reset}   {GREEN}****      ****{reset}
          {RED}###  ###{reset}      {PURPLE}%%%       %%%%{reset}  {GREEN}****           {reset}
         {RED}###   ####{reset}     {PURPLE}%%%       %%%%{reset}  {GREEN}***            {reset}
        {RED}###    ####{reset}    {PURPLE}%%%%      %%%%{reset}  {GREEN}****            {reset}
       {RED}#############{reset}    {PURPLE}%%%      %%%%{reset}   {GREEN}****       ***{reset}  
      {RED}####       ###{reset}   {PURPLE}%%%%%%%%%%%%{reset}     {GREEN} ************{reset}   
     {RED}####        ####{reset}  {PURPLE}%%%%%%%%%{reset}          {GREEN}*******{reset}  

        | ADC Archiver {CYAN}Aurora{reset} | Version 2025.05.2 | byte-key: 8 |

        
        GitHub page: https://github.com/Mealman1551/ADC
        Webpage: https://mealman1551.github.io/adc.html
        Webpage 2: https://mealman1551.github.io/ADC
        E-mail: adc@linuxmail.org


        You are using ADC on: {YELLOW}{dev}{reset}
        You are using ADC as: {YELLOW}{name}{reset}
        You are using ADC on: {YELLOW}{opr}{reset}

        (c) 2025 Mealman1551
        """

        print(info)
    
    elif command == 'q' or command == 'exit' or command == 'quit':
        print("Thank you for using ADC Archiver {CYAN}Aurora{reset}!")
        break

    else:
        print("Invalid command. Please type 'c' to create, 'e' to extract, 'i' for info or 'q' to quit.")
main()