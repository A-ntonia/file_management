import os

def add_new_empty_file(file_name):
    if file_name in os.listdir():
        print(f'{file_name} already exists in the directory')
    else:
        os.system(f'touch {file_name}')

def new_file_with_content(file_name, content):
    if file_name in os.listdir():
        print(f'{file_name} already exists in the directory')
    else:
        with open(file_name, 'w') as file:
            file.write(content)

def rename_file(previous_name, new_name):
    if new_name in os.listdir():
        print(f'{new_name} already exists in the directory')
    elif previous_name not in os.listdir():
        print(f'{previous_name} does not exist in the directory')
    else:
        os.rename(previous_name, new_name)

def remove_folder(folder_name):
    if folder_name in os.listdir():
        os.remove(folder_name)
    else:
        print(f'{folder_name} does not exist in the directory')

def copy_file(file_name, copied_file_name):
    if file_name not in os.listdir():
        print(f'{file_name} does not exist in the directory')
    elif copied_file_name in os.listdir():
        print(f'{copied_file_name} already exists in the directory')
    else:
        os.system(f'cp {file_name} {copied_file_name}')

def list_files_and_folders():
    print(os.listdir())

