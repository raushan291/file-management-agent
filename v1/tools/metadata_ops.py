import os

# file metadata
def get_file_size(filename: str) -> str:
    """
    Returns the size of the specified file in bytes.
    Args:
        filename: The name of the file to check (e.g., 'file.txt').
    Returns:
        A message containing the file size or describing the error.
    """
    
    if not os.path.isfile(filename):
        return f"Error: File '{filename}' does not exist."
    size = os.path.getsize(filename)
    return f"Size of file '{filename}': {size} bytes."

def get_folder_size(folder_path: str) -> str:
    """
    Returns the size of the specified folder in bytes.
    Args:
        folder_path: The path of the folder to check (e.g., '/home/user/documents').
    Returns:
        A message containing the folder size or describing the error.
    """
    
    if not os.path.isdir(folder_path):
        return f"Error: Folder '{folder_path}' does not exist."
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return f"Size of folder '{folder_path}': {total_size} bytes."

def get_file_info(filename: str) -> str:
    """
    Returns information about the specified file.
    Args:
        filename: The name of the file to check (e.g., 'file1.txt').
    Returns:
        A message containing the file information or describing the error.
    """
    
    if not os.path.isfile(filename):
        return f"Error: File '{filename}' does not exist."
    stat_info = os.stat(filename)
    return f"File '{filename}' information:\nSize: {stat_info.st_size} bytes\nLast Modified: {stat_info.st_mtime}"

def get_last_modified(filename: str) -> str:
    """
    Returns the last modified timestamp of the specified file.
    Args:
        filename: The name of the file to check (e.g., 'file1.txt').
    Returns:
        A message containing the last modified timestamp or describing the error.
    """
    
    if not os.path.isfile(filename):
        return f"Error: File '{filename}' does not exist."
    last_modified = os.path.getmtime(filename)
    return f"Last modified time of file '{filename}': {last_modified}"

def get_permissions(path: str) -> str:
    """
    Returns the permissions of the specified path.
    Args:
        path: The path of the file or folder to check (e.g., '/home/user/documents').
    Returns:
        A message containing the permissions or describing the error.
    """
    
    if not os.path.exists(path):
        return f"Error: Path '{path}' does not exist."
    permissions = oct(os.stat(path).st_mode)[-3:]
    return f"Permissions of '{path}': {permissions}"
