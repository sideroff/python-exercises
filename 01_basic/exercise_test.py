from os import listdir, rename
from os.path import isfile, join

def custom_rename(dir_path: str, prefix: str):
    for file_name in listdir(dir_path):
        if isfile(join(dir_path, file_name)):
            rename(file_name, prefix + file_name)