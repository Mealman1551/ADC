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