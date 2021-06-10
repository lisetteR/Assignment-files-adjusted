__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os
import shutil
import zipfile
import os.path


current_path = os.getcwd()
folder = "cache"

def clean_cache():
    if not os.path.exists('./cache'):
        os.makedirs(os.path.realpath(folder))  
    else:
        try:
            shutil.rmtree(os.path.realpath(folder))
        except OSError as e:
            print(e)
    return
print(clean_cache())


def cache_zip(zip_file_path: str, cache_dir_path: str):
    from zipfile import ZipFile
    with zipfile.ZipFile(zip_file_path, 'r') as files_unzip:
        files_unzip.extractall(cache_dir_path)
    return files_unzip


def cached_files():
    list_files = os.listdir(os.path.realpath(folder))
    absolute_list_files = []
    for file in list_files:
        absolute_list_files.append(os.path.join(os.path.realpath(folder), file))
    return absolute_list_files


def find_password(cached_files: list):
    for file in cached_files:
        with open(file, 'r') as f:
            read_line = f.read().split("\n")
            for line in read_line:
                if "password" in line:
                    password_line = line
                    password = password_line.split(": ")[-1]
                else:
                    continue
    return password
