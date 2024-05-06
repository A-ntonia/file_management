import os

def add_new_folder(folder_path, folder_name):
    """
    Create a new folder in the specified directory.

    Args:
        folder_path (str): The path of the directory where the new folder will be created.
        folder_name (str): The name of the new folder.

    Returns:
        None

    Raises:
        None
    """
    if os.path.isdir(folder_path) == False:
        print(f'This folder path: {folder_path} does not exist')
        return
    elif folder_name in os.listdir(folder_path):
        print(f'Folder name: {folder_name} already exists in the directory')
        return
    else:
        os.mkdir(f'{folder_path}/{folder_name}')

def remove_folder(folder_path, folder_name):
    """
    Remove a folder from the specified directory.

    Args:
        folder_path (str): The path of the directory containing the folder.
        folder_name (str): The name of the folder to be removed.

    Returns:
        None

    Raises:
        None
    """
    if os.path.isdir(folder_path) == False:
        print(f'This folder path: {folder_path} does not exist')
        return
    elif folder_name not in os.listdir(folder_path):
        print(f'Folder: {folder_name} does not exist in the directory')
        return
    else:
        os.rmdir(f'{folder_path}/{folder_name}')

def rename_folder(folder_path, old_folder_name, new_folder_name):
    """
    Renames a folder in the specified directory.

    Args:
        folder_path (str): The path to the directory containing the folder.
        old_folder_name (str): The current name of the folder.
        new_folder_name (str): The new name for the folder.

    Returns:
        None

    Raises:
        None
    """
    if os.path.isdir(folder_path) == False:
        print(f'This folder path: {folder_path} does not exist')
        return
    elif old_folder_name not in os.listdir(folder_path):
        print(f'Folder: {old_folder_name} does not exist in the directory')
        return
    elif new_folder_name in os.listdir(folder_path):
        print(f'A folder with this name: {new_folder_name} already exists in the directory')
        return
    else:
        os.rename(f'{folder_path}/{old_folder_name}', f'{folder_path}/{new_folder_name}')

def copy_folder(folder_path, folder_name, copied_folder_name):
    """
    Copies a folder to a new location.

    Args:
        folder_path (str): The path of the folder.
        folder_name (str): The name of the folder to be copied.
        copied_folder_name (str): The name of the copied folder.

    Returns:
        None
    """
    if os.path.isdir(folder_path) == False:
        print(f'This folder path: {folder_path} does not exist')
        return
    elif folder_name not in os.listdir(folder_path):
        print(f'Folder: {folder_name} does not exist in the directory')
        return
    else:
        os.system(f'cp -r {folder_path}/{folder_name} {folder_path}/{copied_folder_name}')
