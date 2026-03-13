import os


# monitoring
def watch_folder(folder_path: str) -> str:
    """
    Watches a folder for changes and reports any new files added.
    Args:
        folder_path: The path of the folder to watch (e.g., './' for current directory).
    Returns:
        A message confirming that the folder is being watched or describing the error.
    """

    if not os.path.isdir(folder_path):
        return f"Error: Folder '{folder_path}' does not exist."
    return f"Watching folder: '{folder_path}' for changes. (Note: This is a placeholder function.)"

def file_exists(filename: str) -> str:
    """
    Checks if a file exists.
    Args:
        filename: The name of the file to check.
    Returns:
        A message confirming if the file exists or describing the error.
    """
    
    if not os.path.exists(filename):
        return f"Error: File '{filename}' does not exist."
    return f"File '{filename}' exists."

def folder_exists(folder_name: str) -> str:
    """
    Checks if a folder exists.
    Args:
        folder_name: The name of the folder to check.
    Returns:
        A message confirming if the folder exists or describing the error.
    """
    
    if not os.path.exists(folder_name):
        return f"Error: Folder '{folder_name}' does not exist."
    return f"Folder '{folder_name}' exists."

# advanced useful  operations
def get_disk_usage(folder_path: str) -> str:
    """ 
    Gets the disk usage of a folder.
    Args:
        folder_path: The path of the folder to check.
    Returns:
        A message confirming the disk usage or describing the error.
    """
    
    if not os.path.exists(folder_path):
        return f"Error: Folder '{folder_path}' does not exist."
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return f"Disk usage for '{folder_path}': {total_size} bytes."

def get_current_directory() -> str:
    """
    Gets the current working directory.
    Returns:
        A message containing the current directory path or describing the error.
    """
    
    try:
        cwd = os.getcwd()
        return f"Current working directory: '{cwd}'."
    except Exception as e:
        return f"Error getting current directory: {e}"

def change_directory(folder_path: str) -> str:
    """
    Changes the current working directory.
    Args:
        folder_path: The path of the folder to change to.
    Returns:
        A message confirming the directory change or describing the error.
    """
    
    if not os.path.exists(folder_path):
        return f"Error: Folder '{folder_path}' does not exist."
    os.chdir(folder_path)
    return f"Changed directory to: '{folder_path}'."

def get_directory_tree(folder_path: str) -> str:
    """
    Gets a tree view of the directory structure starting from the specified folder.
    Args:
        folder_path: The path of the folder to generate the tree view from.
    Returns:
        A message containing the directory tree or describing the error.
    """

    if not os.path.exists(folder_path):
        return f"Error: Folder '{folder_path}' does not exist."
    tree = ""
    for dirpath, dirnames, filenames in os.walk(folder_path):
        level = dirpath.replace(folder_path, '').count(os.sep)
        indent = ' ' * 4 * level
        tree += f"{indent}{os.path.basename(dirpath)}/\n"
        subindent = ' ' * 4 * (level + 1)
        for filename in filenames:
            tree += f"{subindent}{filename}\n"
    return f"Directory tree for '{folder_path}':\n{tree}"

def get_recent_files(folder_path: str, n: int) -> str:
    """
    Gets the most recently modified files in a folder.
    Args:
        folder_path: The path of the folder to search.
        n: The number of recent files to return.
    Returns:
        A message containing the list of recent files or describing the error.
    """
    
    if not os.path.exists(folder_path):
        return f"Error: Folder '{folder_path}' does not exist."
    files = []
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isfile(filepath):
            files.append((filepath, os.path.getmtime(filepath)))
    files.sort(key=lambda x: x[1], reverse=True)
    recent_files = [os.path.basename(filepath) for filepath, _ in files[:n]]
    return f"Recent files in '{folder_path}': {', '.join(recent_files)}"

def normalize_path(path: str) -> str:
    """
    Normalizes a file path to an absolute path.
    Args:
        path: The file path to normalize.
    Returns:
        A message containing the normalized path or describing the error.
    """
    
    try:
        normalized_path = os.path.abspath(path)
        return f"Normalized path: '{normalized_path}'."
    except Exception as e:
        return f"Error normalizing path: {e}"

def get_absolute_path(path: str) -> str:
    """
    Gets the absolute path of a file or directory.
    Args:
        path: The file or directory path.
    Returns:
        A message containing the absolute path or describing the error.
    """
    
    try:
        abs_path = os.path.abspath(path)
        return f"Absolute path: '{abs_path}'."
    except Exception as e:
        return f"Error getting absolute path: {e}"


# bulk operations
def batch_rename(folder_path: str, prefix: dict) -> str:
    """
    Renames all files in a folder by adding a prefix.
    Args:
        folder_path: The path of the folder containing the files to rename.
        prefix: The prefix to add to each file name.
    Returns:
        A message confirming the renaming or describing the error.
    """

    if not os.path.exists(folder_path):
        return f"Error: Folder '{folder_path}' does not exist."
    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, prefix + filename)
        os.rename(old_path, new_path)
    return f"Renamed all files in '{folder_path}' with prefix '{prefix}'."

def copy_multiple(files: list, dst: str) -> str:
    """
    Copies multiple files to a new location.
    Args:
        files: A list of file paths to copy.
        dst: The destination folder path.
    Returns:
        A message confirming the copying or describing the error.
    """

    if not os.path.exists(dst):
        return f"Error: Destination folder '{dst}' does not exist."
    for file in files:
        if not os.path.exists(file):
            return f"Error: File '{file}' does not exist."
        os.system(f"cp {file} {dst}")
    return f"Copied files {files} to '{dst}'."
