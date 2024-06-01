import unittest
import os
import pandas as pd
from Project import export_to_csv, export_to_excel

class TestExportToCSVAndExcel(unittest.TestCase):
    def setUp(self):
        self.test_data = [
            {'File Name': 'file1.txt', 'File Size (in bytes)': 13},
            {'File Name': 'file2.txt', 'File Size (in bytes)': 20}
        ]
        self.test_df = pd.DataFrame(self.test_data)

    def test_export_to_csv(self):
        output_file = 'test_folder_info.csv'
        export_to_csv(self.test_df, output_file)
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)

    def test_export_to_excel(self):
        output_file = 'test_folder_info.xlsx'
        export_to_excel(self.test_df, output_file)
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)
