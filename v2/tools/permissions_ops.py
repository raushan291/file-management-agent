import os


# permissions and ownership
def change_permissions(path: str, mode: str) -> str:
    """
    Changes the permissions of the specified path.
    Args:
        path: The path of the file or folder to modify (e.g., '/home/user/documents').
        mode: The new permissions to set (e.g., '644').
    Returns:
        A message indicating the success or failure of the operation.
    """
    
    if not os.path.exists(path):
        return f"Error: Path '{path}' does not exist."
    try:
        os.chmod(path, int(mode, 8))
        return f"Permissions of '{path}' changed to {mode}."
    except Exception as e:
        return f"Error changing permissions of '{path}': {e}"

def change_owner(path: str, user: str) -> str:
    """
    Changes the owner of the specified path.
    Args:
        path: The path of the file or folder to modify (e.g., '/home/user/documents').
        user: The new owner to set (e.g., 'john').
    Returns:
        A message indicating the success or failure of the operation.
    """
    
    if not os.path.exists(path):
        return f"Error: Path '{path}' does not exist."
    try:
        os.chown(path, uid=os.getpwnam(user).pw_uid, gid=os.getpwnam(user).pw_gid)
        return f"Owner of '{path}' changed to {user}."
    except Exception as e:
        return f"Error changing owner of '{path}': {e}"

# cleanup utilities
def delete_by_extension(folder_path: str, extension: str) -> str:
    """
    Deletes files with the specified extension from the given folder.
    Args:
        folder_path: The path of the folder to search (e.g., '/home/user/documents').
        extension: The file extension to delete (e.g., '.txt').
    Returns:
        A message indicating the success or failure of the operation.
    """
    
    if not os.path.isdir(folder_path):
        return f"Error: Folder '{folder_path}' does not exist."
    deleted_files = []
    for filename in os.listdir(folder_path):
        if filename.endswith(extension):
            file_path = os.path.join(folder_path, filename)
            os.remove(file_path)
            deleted_files.append(filename)
    return f"Deleted files with extension '{extension}': {deleted_files}"

def remove_empty_folders(folder_path: str) -> str:
    """
    Removes empty folders from the given folder.
    Args:
        folder_path: The path of the folder to search (e.g., '/home/user/documents').
    Returns:
        A message indicating the success or failure of the operation.
    """
    
    if not os.path.isdir(folder_path):
        return f"Error: Folder '{folder_path}' does not exist."
    removed_folders = []
    for dirpath, dirnames, filenames in os.walk(folder_path, topdown=False):
        for dirname in dirnames:
            folder_to_check = os.path.join(dirpath, dirname)
            if not os.listdir(folder_to_check):
                os.rmdir(folder_to_check)
                removed_folders.append(folder_to_check)
    return f"Removed empty folders: {removed_folders}"

def clear_file(filename: str) -> str:
    """
    Clears the contents of the specified file.
    Args:
        filename: The name of the file to clear (e.g., 'file1.txt').
    Returns:
        A message indicating the success or failure of the operation.
    """
    
    if not os.path.isfile(filename):
        return f"Error: File '{filename}' does not exist."
    try:
        with open(filename, 'w') as f:
            f.truncate(0)
        return f"File '{filename}' cleared."
    except Exception as e:
        return f"Error clearing file '{filename}': {e}"
