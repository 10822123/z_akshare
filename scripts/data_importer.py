import os
import glob

def import_data_from_folder(folder_path, file_extension='*.*'):
    file_list = glob.glob(os.path.join(folder_path, file_extension))
    all_data = []

    for file_path in file_list:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()
            all_data.append(data)

    return all_data
