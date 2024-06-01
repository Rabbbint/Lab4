import os
import pandas as pd
from datetime import datetime
from zoneinfo import ZoneInfo

def collect_folder_info(folder_path):
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_info = {
                'File Name': file,
                'File Path': file_path,
                'File Size (in bytes)': os.path.getsize(file_path),
                'Creation Time': convert_to_moscow_time(os.path.getctime(file_path)).replace(tzinfo=None),
                'Last Access Time': convert_to_moscow_time(os.path.getatime(file_path)).replace(tzinfo=None),
                'Last Modification Time': convert_to_moscow_time(os.path.getmtime(file_path)).replace(tzinfo=None)
            }
            file_list.append(file_info)
    return file_list

def convert_to_moscow_time(timestamp):
    utc_tz = ZoneInfo('UTC')
    moscow_tz = ZoneInfo('Europe/Moscow')
    utc_time = datetime.utcfromtimestamp(timestamp)
    utc_time = utc_time.replace(tzinfo=utc_tz)
    moscow_time = utc_time.astimezone(moscow_tz)
    return moscow_time

def export_to_csv(df, output_file):
    df.to_csv(output_file, index=False)

def export_to_excel(df, output_file):
    df.to_excel(output_file, index=False)
