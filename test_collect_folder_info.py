import unittest
import os
import tempfile
from utils import collect_folder_info

class TestCollectFolderInfo(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.create_test_files()

    def tearDown(self):
        self.temp_dir.cleanup()

    def create_test_files(self):
        self.test_file1 = os.path.join(self.temp_dir.name, 'file1.txt')
        self.test_file2 = os.path.join(self.temp_dir.name, 'file2.txt')
        with open(self.test_file1, 'w') as f:
            f.write('Hello, world!')
        with open(self.test_file2, 'w') as f:
            f.write('This is a test file.')

    def test_collect_folder_info(self):
        file_list = collect_folder_info(self.temp_dir.name)
        self.assertEqual(len(file_list), 2)
        self.assertIn({'File Name': 'file1.txt', 'File Path': os.path.join(self.temp_dir.name, 'file1.txt'),
                       'File Size (in bytes)': 13, 'Creation Time': file_list[0]['Creation Time'],
                       'Last Access Time': file_list[0]['Last Access Time'],
                       'Last Modification Time': file_list[0]['Last Modification Time']}, file_list)


