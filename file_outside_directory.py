import os

def add_new_file(folder_path, file_name):
    if os.path.isdir(folder_path) == False:
        print(f'This folder path: {folder_path} does not exist')
        return
    elif file_name in os.listdir(folder_path):
        print(f'{file_name} already exists in the directory')
        return
    else:
        os.system(f'touch {folder_path}/{file_name}')

def add_new_file_with_content(folder_path, file_name, content):
    if os.path.isdir(folder_path) == False:
        print(f'This folder path: {folder_path} does not exist')
        return
    elif file_name in os.listdir(folder_path):
        print(f'This file name: {file_name} already exists in the directory')
        return
    else:
        with open(f'{folder_path}/{file_name}', 'w') as file:
            file.write(content)

def rename_file(folder_path, previous_name, new_name):
    if os.path.isdir(folder_path) == False:
        print(f'This folder path: {folder_path} does not exist')
        return
    elif previous_name not in os.listdir(folder_path):
        print(f'{previous_name} does not exist in the directory')
        return
    elif new_name in os.listdir(folder_path):
        print(f'{new_name} already exists in the directory')
        return
    else:
        os.rename(f'{folder_path}/{previous_name}', f'{folder_path}/{new_name}')

def delete_file(folder_path, file_name):
    if os.path.isdir(folder_path) == False:
        print(f'This folder path: {folder_path} does not exist')
        return
    elif file_name not in os.listdir(folder_path):
        print(f'{file_name} does not exist in the directory')
        return
    else:
        os.remove(f'{folder_path}/{file_name}')

def copy_file(folder_path, file_name, copied_file_name):
    if os.path.isdir(folder_path) == False:
        print(f'This folder path: {folder_path} does not exist')
        return
    elif file_name not in os.listdir(folder_path):
        print(f'{file_name} does not exist in the directory')
        return
    elif copied_file_name in os.listdir(folder_path):
        print(f'{copied_file_name} already exists in the directory')
        return
    else:
        os.system(f'cp {folder_path}/{file_name} {folder_path}/{copied_file_name}')