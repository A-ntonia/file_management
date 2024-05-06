import os

def add_new_file(folder_path, file_name):
    """
    Create a new file in the specified folder path with the given file name.

    Args:
        folder_path (str): The path of the folder where the file will be created.
        file_name (str): The name of the file to be created.

    Returns:
        None
    """
    if os.path.isdir(folder_path) == False:
        print(f'This folder path: {folder_path} does not exist')
        return
    elif file_name in os.listdir(folder_path):
        print(f'File name: {file_name} already exists in the directory')
        return
    else:
        os.system(f'touch {folder_path}/{file_name}')

def add_new_file_with_content(folder_path, file_name, content):
    """
    Create a new file with the specified file name and content in the given folder path.

    Args:
        folder_path (str): The path of the folder where the file will be created.
        file_name (str): The name of the file to be created.
        content (str): The content to be written to the file.

    Returns:
        None

    Raises:
        None
    """
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
    """
    Renames a file in the specified folder path.

    Args:
        folder_path (str): The path of the folder where the file is located.
        previous_name (str): The current name of the file.
        new_name (str): The new name to be assigned to the file.

    Returns:
        None
    """
    if os.path.isdir(folder_path) == False:
        print(f'This folder path: {folder_path} does not exist')
        return
    elif previous_name not in os.listdir(folder_path):
        print(f'File: {previous_name} does not exist in the directory')
        return
    elif new_name in os.listdir(folder_path):
        print(f'A file with this name: {new_name} already exists in the directory')
        return
    else:
        os.rename(f'{folder_path}/{previous_name}', f'{folder_path}/{new_name}')

def delete_file(folder_path, file_name):
    """
    Deletes a file from the specified folder path.

    Args:
        folder_path (str): The path of the folder where the file is located.
        file_name (str): The name of the file to be deleted.

    Returns:
        None

    Raises:
        None
    """
    if os.path.isdir(folder_path) == False:
        print(f'This folder path: {folder_path} does not exist')
        return
    elif file_name not in os.listdir(folder_path):
        print(f'File: {file_name} does not exist in the directory')
        return
    else:
        os.remove(f'{folder_path}/{file_name}')

def copy_file(folder_path, file_name, copied_file_name):
    """
    Copies a file from a specified folder to the same folder with a new name.

    Args:
        folder_path (str): The path of the folder where the file is located.
        file_name (str): The name of the file to be copied.
        copied_file_name (str): The new name for the copied file.

    Returns:
        None
    """
    if os.path.isdir(folder_path) == False:
        print(f'This folder path: {folder_path} does not exist')
        return
    elif file_name not in os.listdir(folder_path):
        print(f'File: {file_name} does not exist in the directory')
        return
    elif copied_file_name in os.listdir(folder_path):
        print(f'A file with this name: {copied_file_name} already exists in the directory')
        return
    else:
        os.system(f'cp {folder_path}/{file_name} {folder_path}/{copied_file_name}')