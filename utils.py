import os
import datetime
import pandas as pd

def collect_folder_info(folder_path):
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_stats = os.stat(file_path)
            file_info = {
                "Имя файла": file,
                "Размер (байт)": file_stats.st_size,
                "Дата модификации": datetime.datetime.fromtimestamp(file_stats.st_mtime),
                "Дата создания": datetime.datetime.fromtimestamp(file_stats.st_ctime),
                "Путь к файлу": file_path
            }
            file_list.append(file_info)
    return file_list

def convert_to_moscow_time(file_list):
    moscow_tz = datetime.timezone(datetime.timedelta(hours=3))
    for file_info in file_list:
        file_info["Дата модификации"] = file_info["Дата модификации"].astimezone(moscow_tz)
        file_info["Дата создания"] = file_info["Дата создания"].astimezone(moscow_tz)
    return file_list

def export_to_csv(file_list, output_file):
    df = pd.DataFrame(file_list)
    df.to_csv(output_file, index=False)

def export_to_excel(file_list, output_file):
    df = pd.DataFrame(file_list)
    df.to_excel(output_file, index=False)
