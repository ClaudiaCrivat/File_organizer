import os
import shutil

def menu():
    path = input ('Insert the path or press X to exit the program: ')
    while not path_validation(path):
        if path == 'X':
            exit()
        path = input('Insert the path or press X to exit the program:')
    print('The path is valid')
    return path

def path_validation(path: str) -> bool:
    return os.path.isdir(path)

def create_dirs(path: str):
    for dir in DIR_TYPES:
        if not os.path.isdir(path + '\\' + dir):
            os.mkdir(path+ '\\' + dir)

def list_all_files(path: str) -> list:
    files = [file for file in os.listdir(path) if os.path.isfile(path + '\\' + file)]
    return files

def extract_file_extension(file: str) -> str:
    indexes = [i for i, ch in enumerate(file) if ch == '.']
    if indexes:
        file_extension = file[indexes[-1]::]
        return file_extension
    else:
        return 'no extension'

def map_extension_to_folder(path:str) -> dict:
    extension_mapping = {path + '\\' + dir:FILE_EXT_TYPES[i] for i, dir in enumerate(DIR_TYPES)}
    return extension_mapping

if __name__ == '__main__':
    DIR_TYPES = ['Pictures', 'Videos', 'PDF',
                 'TXT', 'Python','Word', 'Archived']
    FILE_EXT_TYPES = [['.jpg', '.jpeg', '.png', '.JPG'],
                      ['.mp4', '.avi'], ['.pdf', '.PDF'],
                      '.txt', '.py', ['.doc', '.docx'], '.zip']
    path = menu()
    mapping = map_extension_to_folder(path)
    print(mapping)
    create_dirs(path)
    files = list_all_files(path)
    print(files)
    for file in files:
        file_extension = extract_file_extension(file)
        for k, v in mapping.items():
            if file_extension in v:
                try:
                    shutil.move(path + '\\' + file, k)
                except:
                    print(file + 'cannot be moved!')