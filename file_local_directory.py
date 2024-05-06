import os

def add_new_empty_file(file_name):
    """
    Create a new empty file with the given file name.

    Args:
        file_name (str): The name of the file to be created.

    Returns:
        None
    """
    if file_name in os.listdir():
        print(f'{file_name} already exists in the directory')
    else:
        os.system(f'touch {file_name}')

def new_file_with_content(file_name, content):
    """
    Create a new file with the given file name and write the provided content to it.

    Args:
        file_name (str): The name of the file to be created.
        content (str): The content to be written to the file.

    Returns:
        None
    """
    if file_name in os.listdir():
        print(f'{file_name} already exists in the directory')
    else:
        with open(file_name, 'w') as file:
            file.write(content)

def rename_file(previous_name, new_name):
    """
    Renames a file in the current directory.

    Args:
        previous_name (str): The name of the file to be renamed.
        new_name (str): The new name for the file.

    Returns:
        None

    Raises:
        None
    """
    if new_name in os.listdir():
        print(f'{new_name} already exists in the directory')
    elif previous_name not in os.listdir():
        print(f'{previous_name} does not exist in the directory')
    else:
        os.rename(previous_name, new_name)

def remove_folder(folder_name):
    """
    Removes a folder from the current directory.

    Args:
        folder_name (str): The name of the folder to be removed.

    Returns:
        None

    Raises:
        None
    """
    if folder_name in os.listdir():
        os.remove(folder_name)
    else:
        print(f'{folder_name} does not exist in the directory')

def copy_file(file_name, copied_file_name):
    """
    Copy a file to a new location.

    Args:
        file_name (str): The name of the file to be copied.
        copied_file_name (str): The name of the copied file.

    Returns:
        None
    """
    if file_name not in os.listdir():
        print(f'{file_name} does not exist in the directory')
    elif copied_file_name in os.listdir():
        print(f'{copied_file_name} already exists in the directory')
    else:
        os.system(f'cp {file_name} {copied_file_name}')

def list_files_and_folders():
    """
    Lists all the files and folders in the current directory.
    """
    print(os.listdir())

