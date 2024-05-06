import os

def add_new_folder(folder_name):
    if folder_name in os.listdir():
        print(f'{folder_name} already exists in the directory')
    else:
        os.mkdir(f'{folder_name}')

def remove_folder(folder_name):
    if(folder_name not in os.listdir()):
        print(f'{folder_name} does not exist in the directory')
    else:
        os.rmdir(f'{folder_name}')

def rename_folder(previous_name, new_name):
    if(previous_name not in os.listdir()):
        print(f'{previous_name} does not exist in the directory')
    elif(new_name in os.listdir()):
        print(f'{new_name} already exists in the directory')
    else:
        os.rename(previous_name, new_name)

def copy_folder(folder_name, copied_folder_name):
    if folder_name not in os.listdir():
        print(f'{folder_name} does not exist in the directory')
    elif copied_folder_name in os.listdir():
        print(f'{copied_folder_name} already exists in the directory')
    else:
        os.system(f'cp {folder_name} {copied_folder_name}')