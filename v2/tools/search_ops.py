import os

# search and filter
def search_file_by_name(folder_path: str, pattern: str) -> str:
    """
    Searches for files in the specified folder that contain the given pattern in their name.
    Args:
        folder_path: The path of the folder to search (e.g., '/home/user/documents').
        pattern: The pattern to search for in file names (e.g., 'report').
    Returns:
        A message containing the list of matching files or describing the error.
    """

    if not os.path.isdir(folder_path):
        return f"Error: Folder '{folder_path}' does not exist."
    found_files = []
    for filename in os.listdir(folder_path):
        if pattern in filename:
            found_files.append(filename)
    return f"Files containing '{pattern}': {found_files}"

def search_by_extension(folder_path: str, extension: str) -> str:
    """
    Searches for files in the specified folder with the given extension.
    Args:
        folder_path: The path of the folder to search (e.g., '/home/user/documents').
        extension: The file extension to search for (e.g., '.txt').
    Returns:
        A message containing the list of matching files or describing the error.
    """
    
    if not os.path.isdir(folder_path):
        return f"Error: Folder '{folder_path}' does not exist."
    found_files = []
    for filename in os.listdir(folder_path):
        if filename.endswith(extension):
            found_files.append(filename)
    return f"Files with extension '{extension}': {found_files}"

def search_in_file(filename: str, keyword: str) -> str:
    """
    Searches for a keyword in the specified file.
    Args:
        filename: The name of the file to search (e.g., 'file1.txt').
        keyword: The keyword to search for (e.g., 'error').
    Returns:
        A message indicating whether the keyword was found or describing the error.
    """
    
    if not os.path.isfile(filename):
        return f"Error: File '{filename}' does not exist."
    try:
        with open(filename, 'r') as f:
            content = f.read()
            if keyword in content:
                return f"Keyword '{keyword}' found in file '{filename}'."
            else:
                return f"Keyword '{keyword}' not found in file '{filename}'."
    except Exception as e:
        return f"Error searching in file '{filename}': {e}"

def search_in_directory(folder_path: str, keyword: str) -> str:
    """
    Searches for a keyword in all files within the specified directory.
    Args:
        folder_path: The path of the directory to search (e.g., '/home/user/documents').
        keyword: The keyword to search for (e.g., 'error').
    Returns:
        A message indicating whether the keyword was found or describing the error.
    """
    
    if not os.path.isdir(folder_path):
        return f"Error: Folder '{folder_path}' does not exist."
    found_files = []
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    if keyword in content:
                        found_files.append(file_path)
            except Exception as e:
                return f"Error reading file '{file_path}': {e}"
    return f"Keyword '{keyword}' found in files: {found_files}"
