import unittest
import datetime
import os
import tempfile
import pandas as pd
from io import StringIO
from utils import collect_folder_info, convert_to_moscow_time, export_to_csv, export_to_excel

class TestUtils(unittest.TestCase):
    def setUp(self):
        # Создание временной директории для тестирования
        self.temp_dir = tempfile.TemporaryDirectory()
        # Создание файлов для тестирования
        with open(os.path.join(self.temp_dir.name, 'file1.txt'), 'w') as f:
            f.write('Hello, world!')
        with open(os.path.join(self.temp_dir.name, 'file2.txt'), 'w') as f:
            f.write('Goodbye, world!')

    def tearDown(self):
        # Удаление временной директории
        self.temp_dir.cleanup()

    def test_collect_folder_info(self):
        file_list = collect_folder_info(self.temp_dir.name)
        self.assertEqual(len(file_list), 2)
        self.assertIn({'File Name': 'file1.txt', 'File Path': os.path.join(self.temp_dir.name, 'file1.txt'),
                       'File Size (in bytes)': 13, 'Creation Time': file_list[0]['Creation Time'],
                       'Last Access Time': file_list[0]['Last Access Time'],
                       'Last Modification Time': file_list[0]['Last Modification Time']}, file_list)
        self.assertIn({'File Name': 'file2.txt', 'File Path': os.path.join(self.temp_dir.name, 'file2.txt'),
                       'File Size (in bytes)': 13, 'Creation Time': file_list[1]['Creation Time'],
                       'Last Access Time': file_list[1]['Last Access Time'],
                       'Last Modification Time': file_list[1]['Last Modification Time']}, file_list)

    def test_convert_to_moscow_time(self):
        file_list = [
            {"Last Modification Time": datetime.datetime(2023, 4, 1, 12, 0, 0)},
            {"Last Modification Time": datetime.datetime(2023, 4, 1, 15, 0, 0)}
        ]

        converted_list = [convert_to_moscow_time(file['Last Modification Time'].timestamp()) for file in file_list]

        self.assertEqual(converted_list[0], datetime.datetime(2023, 4, 1, 15, 0, 0))
        self.assertEqual(converted_list[1], datetime.datetime(2023, 4, 1, 18, 0, 0))

    def test_export_to_csv(self):
        file_list = [
            {'File Name': 'file1.txt', 'File Path': '/path/to/file1.txt', 'File Size (in bytes)': 13,
             'Creation Time': datetime.datetime(2023, 4, 1, 12, 0, 0),
             'Last Access Time': datetime.datetime(2023, 4, 1, 12, 0, 1),
             'Last Modification Time': datetime.datetime(2023, 4, 1, 12, 0, 2)},
            {'File Name': 'file2.txt', 'File Path': '/path/to/file2.txt', 'File Size (in bytes)': 14,
             'Creation Time': datetime.datetime(2023, 4, 1, 13, 0, 0),
             'Last Access Time': datetime.datetime(2023, 4, 1, 13, 0, 1),
             'Last Modification Time': datetime.datetime(2023, 4, 1, 13, 0, 2)}
        ]
        df = pd.DataFrame(file_list)

        with StringIO() as csv_buffer:
            export_to_csv(df, csv_buffer)
            csv_content = csv_buffer.getvalue()

        self.assertIn('file1.txt', csv_content)
        self.assertIn('file2.txt', csv_content)
        self.assertIn('2023-04-01 12:00:00', csv_content)
        self.assertIn('2023-04-01 13:00:00', csv_content)

    def test_export_to_excel(self):
        file_list = [
            {'File Name': 'file1.txt', 'File Path': '/path/to/file1.txt', 'File Size (in bytes)': 13,
             'Creation Time': datetime.datetime(2023, 4, 1, 12, 0, 0),
             'Last Access Time': datetime.datetime(2023, 4, 1, 12, 0, 1),
             'Last Modification Time': datetime.datetime(2023, 4, 1, 12, 0, 2)},
            {'File Name': 'file2.txt', 'File Path': '/path/to/file2.txt', 'File Size (in bytes)': 14,
             'Creation Time': datetime.datetime(2023, 4, 1, 13, 0, 0),
             'Last Access Time': datetime.datetime(2023, 4, 1, 13, 0, 1),
             'Last Modification Time': datetime.datetime(2023, 4, 1, 13, 0, 2)}
        ]
        df = pd.DataFrame(file_list)

        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            export_to_excel(df, temp_file.name)
            df_from_excel = pd.read_excel(temp_file.name)

        self.assertEqual(len(df_from_excel), 2)
        self.assertIn('file1.txt', df_from_excel['File Name'].values)
        self.assertIn('file2.txt', df_from_excel['File Name'].values)
        self.assertIn('2023-04-01 12:00:00', df_from_excel['Creation Time'].dt.strftime('%Y-%m-%d %H:%M:%S').values)
        self.assertIn('2023-04-01 13:00:00', df_from_excel['Creation Time'].dt.strftime('%Y-%m-%d %H:%M:%S').values)

