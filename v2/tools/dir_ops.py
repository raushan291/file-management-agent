import os

# directory management
def create_folder(folder_name: str) -> str:
    """
    Create a new directory.

    Args:
        folder_name (str): Name of the folder to create.
    Returns:
        str: Success or error message.
    """
    
    try:
        if os.path.exists(folder_name):
            return f"Error: Folder '{folder_name}' already exists. No action taken."
        else:
            os.makedirs(folder_name)
            return f"Successfully created folder: '{os.path.abspath(folder_name)}'."
    except Exception as e:
        return f"Error creating folder '{folder_name}': {e}"


def create_folder_recursive(path: str) -> str:
    """
    Create a new directory and any necessary parent directories.

    Args:
        path (str): Path of the folder to create.
    Returns:
        str: Success or error message.
    """
    
    try:
        os.makedirs(path)
        return f"Successfully created folder: '{os.path.abspath(path)}'."
    except Exception as e:
        return f"Error creating folder '{path}': {e}"

def delete_folder_recursive(folder_name: str) -> str:
    """
    Delete a directory and all its contents recursively.

    Args:
        folder_name (str): Name of the folder to delete.
    Returns:
        str: Success or error message.
    """
    
    try:
        if not os.path.exists(folder_name):
            return f"Error: Folder '{folder_name}' does not exist."
        os.removedirs(folder_name)
        return f"Successfully deleted folder: '{os.path.abspath(folder_name)}'."
    except Exception as e:
        return f"Error deleting folder '{folder_name}': {e}"

def list_files_recursive(folder_path: str) -> str:
    """
    List all files in a directory and its subdirectories.

    Args:
        folder_path (str): Path of the folder to list.
    Returns:
        str: Formatted string containing all file paths or an error message.
    """
    
    try:
        result = ""
        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                result += f"{os.path.join(root, filename)}\n"
        return result.strip()
    except Exception as e:
        return f"Error listing files in '{folder_path}': {e}"

# copy and move
def copy_folder(src: str, dst: str) -> str:
    """
    Copy a folder and its contents to a new location.
    Args:
        src (str): Source folder path.
        dst (str): Destination folder path.
    Returns:
        str: Success or error message.
    """

    if not os.path.exists(src):
        return f"Error: Source folder '{src}' does not exist."
    if os.path.exists(dst):
        return f"Error: Destination folder '{dst}' already exists."
    os.system(f"cp -r {src} {dst}")
    return f"Successfully copied folder from '{src}' to '{dst}'."

def move_folder(src: str, dst: str) -> str:
    """
    Move a folder and its contents to a new location.
    Args:
        src (str): Source folder path.
        dst (str): Destination folder path.
    Returns:
        str: Success or error message.
    """
    
    if not os.path.exists(src):
        return f"Error: Source folder '{src}' does not exist."
    if os.path.exists(dst):
        return f"Error: Destination folder '{dst}' already exists."
    os.system(f"mv {src} {dst}")
    return f"Successfully moved folder from '{src}' to '{dst}'."
