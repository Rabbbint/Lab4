import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from datetime import datetime
import pytz
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

folder_path = None
folder_df = None

class FolderMonitor(FileSystemEventHandler):
    def on_any_event(self, event):
        if not event.is_directory:
            analyze_folder()

def convert_to_moscow_time(timestamp):
    moscow_tz = pytz.timezone('Europe/Moscow')
    utc_time = datetime.utcfromtimestamp(timestamp)
    utc_time = pytz.utc.localize(utc_time)
    moscow_time = utc_time.astimezone(moscow_tz)
    return moscow_time

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

def display_folder_info_in_tree(tree, file_list):
    tree.delete(*tree.get_children())
    for file_info in file_list:
        tree.insert('', 'end', values=(
            file_info['File Name'],
            file_info['File Path'],
            file_info['File Size (in bytes)'],
            file_info['Creation Time'],
            file_info['Last Access Time'],
            file_info['Last Modification Time']
        ))

def export_to_csv(df, output_file):
    df.to_csv(output_file, index=False)

def export_to_excel(df, output_file):
    df.to_excel(output_file, index=False)

def browse_button():
    global folder_path
    folder_path = filedialog.askdirectory()
    folder_path_label.config(text="Путь к папке: " + folder_path)
    start_monitoring()

def start_monitoring():
    global observer
    observer = Observer()
    event_handler = FolderMonitor()
    observer.schedule(event_handler, folder_path, recursive=True)
    observer.start()
    analyze_folder()

def analyze_folder():
    global folder_df
    file_list = collect_folder_info(folder_path)
    folder_df = pd.DataFrame(file_list)
    display_folder_info_in_tree(tree, file_list)
    completion_label.config(text="Анализ завершен и результаты отображены.")

def export_csv():
    export_to_csv(folder_df, 'folder_info.csv')
    completion_label.config(text="Результаты сохранены в формате CSV.")

def export_excel():
    export_to_excel(folder_df, 'folder_info.xlsx')
    completion_label.config(text="Результаты сохранены в формате Excel.")

# Создание графического интерфейса
root = tk.Tk()
root.title("Программа для анализа содержимого папки")

# Улучшение внешнего вида кнопок и меток
button_style = {'padx': 10, 'pady': 5, 'bg': 'lightblue', 'fg': 'black'}
label_style = {'padx': 10, 'pady': 5, 'bg': 'lightgray', 'fg': 'black'}

browse_button = tk.Button(root, text="Выбрать папку", command=browse_button, **button_style)
browse_button.pack()

folder_path_label = tk.Label(root, text="Путь к папке: ", **label_style)
folder_path_label.pack()

analyze_button = tk.Button(root, text="Проанализировать папку", command=analyze_folder, **button_style)
analyze_button.pack()

export_csv_button = tk.Button(root, text="Экспорт в CSV", command=export_csv, **button_style)
export_csv_button.pack()

export_excel_button = tk.Button(root, text="Экспорт в Excel", command=export_excel, **button_style)
export_excel_button.pack()

completion_label = tk.Label(root, text="", **label_style)
completion_label.pack()

# Добавление Treeview для отображения информации о файлах и подпапках
tree = ttk.Treeview(root, columns=('File Name', 'File Path', 'File Size', 'Creation Time', 'Last Access Time', 'Last Modification Time'))
tree.heading('#0', text='Item')
tree.heading('File Name', text='File Name')
tree.heading('File Path', text='File Path')
tree.heading('File Size', text='File Size')
tree.heading('Creation Time', text='Creation Time')
tree.heading('Last Access Time', text='Last Access Time')
tree.heading('Last Modification Time', text='Last Modification Time')
tree.column('#0', stretch=tk.YES)
tree.column('File Name', stretch=tk.YES)
tree.column('File Path', stretch=tk.YES)
tree.column('File Size', stretch=tk.YES)
tree.column('Creation Time', stretch=tk.YES)
tree.column('Last Access Time', stretch=tk.YES)
tree.column('Last Modification Time', stretch=tk.YES)
tree.pack()

root.mainloop()
