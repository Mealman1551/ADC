import os
import zlib
import tkinter as tk
from tkinter import filedialog
import socket
from time import sleep
from progress.bar import Bar

dev = socket.gethostname()
name = os.getlogin()

def read_binary_file(file_path):
    with open(file_path, 'rb') as file:
        return file.read()

def parma_compress(data):
    return zlib.compress(data)

def parma_decompress(compressed_data):
    return zlib.decompress(compressed_data)

def create_adc_archive(file_paths, output_path):
    with open(output_path, 'wb') as archive_file:
        # Progressbar voor het archiveren
        with Bar('Compressing files...', max=len(file_paths)) as bar:
            for file_path in file_paths:
                filename = os.path.basename(file_path).encode('utf-8')
                original_data = read_binary_file(file_path)
                compressed_data = parma_compress(original_data)
                archive_file.write(len(filename).to_bytes(8, 'big'))
                archive_file.write(filename)
                archive_file.write(len(compressed_data).to_bytes(8, 'big'))
                archive_file.write(compressed_data)
                bar.next()  # Update de progressbar
    print(f"Archive created: {output_path}")

def extract_adc_archive(archive_path, output_dir):
    with open(archive_path, 'rb') as archive_file:
        # Lees bestand en bepaal hoeveel items er in zitten
        file_count = 0
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
            file_count += 1

        # Progressbar voor het uitpakken
        with Bar('Extracting files...', max=file_count) as bar:
            archive_file.seek(0)  # Reset de file pointer naar het begin van het bestand
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
                bar.next()  # Update de progressbar
            print(f"Extraction complete to {output_dir}")

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
    file_path = filedialog.asksaveasfilename(defaultextension=".adc", title="Save ADC archive as")
    return file_path

def open_archive_file():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    file_path = filedialog.askopenfilename(filetypes=[("ADC archives", "*.adc")], title="Select ADC archive to extract")
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
        info = f"""
             ####        %%%%%%%%%%%         ********  
            ######       %%%%%%%%%%%%     *************
           ### ###      %%%%      %%%%   ****      ****
          ###  ###      %%%       %%%%  ****           
         ###   ####     %%%       %%%%  ***            
        ###    ####    %%%%      %%%%  ****            
      #############    %%%      %%%%   ****       ***  
     ####       ###   %%%%%%%%%%%%%     ************   
    ####        ####  %%%%%%%%%%          *******      
                  
                      ADC Aurora
        
    | ADC Archiver | Version 1.2.3.0 (Aurora)| byte-key: 8 |

    You are using ADC on:
    {dev}
    You are using ADC as:
    {name}
    
    Github page: https://github.com/Mealman1551/ADC
    Webpage: https://mealman1551.github.io/adc.html
    Webpage 2: https://mealman1551.github.io/ADC
    e-mail: adc@linuxmail.org
    (c) 2025 Mealman1551   
        
        """
        print(info)
    
    elif command == 'q':
        print("Thank you for using ADC Archiver Aurora!")
        break

    else:
        print("Invalid command. Please type 'c' to create, 'e' to extract, 'i' for info or 'q' to quit.")


if __name__ == "__main__":
    main()
