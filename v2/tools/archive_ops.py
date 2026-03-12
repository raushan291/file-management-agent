import os

# compression and archiving
def zip_folder(folder_path: str, output_zip: str) -> str:
    """
    Compresses a folder into a zip archive.
    Args:
        folder_path: The path of the folder to compress (e.g., '/home/user/documents').
        output_zip: The name of the output zip file (e.g., 'documents.zip').
    Returns:
        A message confirming success or describing the error.
    """
    
    if not os.path.exists(folder_path):
        return f"Error: Folder '{folder_path}' does not exist."
    if os.path.exists(output_zip):
        return f"Error: File '{output_zip}' already exists."
    os.system(f"zip -r {output_zip} {folder_path}")
    return f"Successfully created zip archive: '{output_zip}'."

def unzip_file(zip_path: str, extract_to: str) -> str:
    """
    Extracts a zip file to a specified directory.
    Args:
        zip_path: The path of the zip file to extract (e.g., 'documents.zip').
        extract_to: The directory to extract the contents to (e.g., '/home/user/extracted').
    Returns:
        A message confirming success or describing the error.
    """
    
    if not os.path.exists(zip_path):
        return f"Error: File '{zip_path}' does not exist."
    if not os.path.exists(extract_to):
        return f"Error: Directory '{extract_to}' does not exist."
    os.system(f"unzip {zip_path} -d {extract_to}")
    return f"Successfully extracted '{zip_path}' to '{extract_to}'."

def create_tar(folder_path: str, output_tar: str) -> str:
    """
    Creates a tar archive of a folder.
    Args:
        folder_path: The path of the folder to archive (e.g., '/home/user/documents').
        output_tar: The name of the output tar file (e.g., 'documents.tar').
    Returns:
        A message confirming success or describing the error.
    """
    
    if not os.path.exists(folder_path):
        return f"Error: Folder '{folder_path}' does not exist."
    if os.path.exists(output_tar):
        return f"Error: File '{output_tar}' already exists."
    os.system(f"tar -cf {output_tar} {folder_path}")
    return f"Successfully created tar archive: '{output_tar}'."

# file comparison
def compare_files(file1: str, file2: str) -> str:
    """
    Compares two files and returns the result.
    Args:
        file1: The path of the first file.
        file2: The path of the second file.
    Returns:
        A message confirming the comparison result or describing the error.
    """
    
    if not os.path.exists(file1):
        return f"Error: File '{file1}' does not exist."
    if not os.path.exists(file2):
        return f"Error: File '{file2}' does not exist."
    os.system(f"diff {file1} {file2}")
    return f"Comparison complete."

def files_are_equal(file1: str, file2: str) -> str:
    """
    Checks if two files are equal.
    Args:
        file1: The path of the first file.
        file2: The path of the second file.
    Returns:
        A message confirming if the files are equal or describing the error.
    """
    
    if not os.path.exists(file1):
        return f"Error: File '{file1}' does not exist."
    if not os.path.exists(file2):
        return f"Error: File '{file2}' does not exist."
    result = os.system(f"diff {file1} {file2}")
    if result == 0:
        return f"Files '{file1}' and '{file2}' are equal."
    else:
        return f"Files '{file1}' and '{file2}' are not equal."
