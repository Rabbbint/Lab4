import os
import pandas as pd
from utils import collect_folder_info, convert_to_moscow_time, export_to_csv, export_to_excel

folder_path = "/путь/к/папке"
file_list = collect_folder_info(folder_path)
folder_df = pd.DataFrame(file_list)

# Дальнейшая логика программы, например:
export_to_csv(folder_df, 'folder_info.csv')
export_to_excel(folder_df, 'folder_info.xlsx')
