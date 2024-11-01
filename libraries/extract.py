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