#This is an example of a test file for ADC 1.2.0

import sys
import os
import tempfile
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from ADC_Archiver_1_2_0 import adc


def test_parma_compress_decompress():
    original_data = b"Testdata1234567890"
    compressed = adc.parma_compress(original_data)
    decompressed = adc.parma_decompress(compressed)
    assert decompressed == original_data

def test_create_and_extract_archive():
    with tempfile.TemporaryDirectory() as temp_dir:
        test_file_path = os.path.join(temp_dir, "testfile.txt")
        with open(test_file_path, "wb") as f:
            f.write(b"Some test content")

        archive_path = os.path.join(temp_dir, "test.adc")

        adc.create_adc_archive([test_file_path], archive_path)

        extract_dir = os.path.join(temp_dir, "extracted")
        os.mkdir(extract_dir)
        adc.extract_adc_archive(archive_path, extract_dir)

        extracted_file = os.path.join(extract_dir, "testfile.txt")
        assert os.path.exists(extracted_file)
        with open(extracted_file, "rb") as f:
            content = f.read()
        assert content == b"Some test content"
