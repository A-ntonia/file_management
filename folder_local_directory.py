import os

def add_new_folder(folder_name):
    """
    Create a new folder in the current directory.

    Parameters:
    folder_name (str): The name of the folder to be created.

    Returns:
    None
    """
    if folder_name in os.listdir():
        print(f'{folder_name} already exists in the directory')
    else:
        os.mkdir(f'{folder_name}')

def remove_folder(folder_name):
    """
    Remove a folder from the current directory.

    Args:
        folder_name (str): The name of the folder to be removed.

    Returns:
        None

    Raises:
        None
    """
    if folder_name not in os.listdir():
        print(f'{folder_name} does not exist in the directory')
    else:
        os.rmdir(folder_name)

def rename_folder(previous_name, new_name):
    """
    Renames a folder in the current directory.

    Args:
        previous_name (str): The name of the folder to be renamed.
        new_name (str): The new name for the folder.

    Returns:
        None

    Raises:
        None
    """
    if previous_name not in os.listdir():
        print(f'{previous_name} does not exist in the directory')
    elif new_name in os.listdir():
        print(f'{new_name} already exists in the directory')
    else:
        os.rename(previous_name, new_name)

def copy_folder(folder_name, copied_folder_name):
    """
    Copy a folder to a new location.

    Args:
        folder_name (str): The name of the folder to be copied.
        copied_folder_name (str): The name of the new copied folder.

    Returns:
        None
    """
    if folder_name not in os.listdir():
        print(f'{folder_name} does not exist in the directory')
    elif copied_folder_name in os.listdir():
        print(f'{copied_folder_name} already exists in the directory')
    else:
        os.system(f'cp {folder_name} {copied_folder_name}')