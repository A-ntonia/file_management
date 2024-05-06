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
    if previous_name in os.listdir():
        print(f'{previous_name} and {new_name}')
        os.rename(previous_name, new_name)
    else:
        print(f'{previous_name} does not exist in the directory')

def list_files():
    print(os.listdir())

