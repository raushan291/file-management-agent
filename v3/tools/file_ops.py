import os

def create_file(filename: str) -> str:
    """
    Creates a new, empty file with the specified name in the current directory.

    Args:
        filename: The name of the file to create (e.g., 'file1.txt').
        
    Returns:
        A success or error message confirming the file status.
    """

    try:
        if os.path.exists(filename):
            return f"Error: File '{filename}' already exists. No action taken."
        else:
            with open(filename, "w") as f:
                pass
            return f"Successfully created empty file: '{os.path.abspath(filename)}'."

    except Exception as e:
        return f"Error creating file '{filename}': {e}"


def delete_file(filename: str) -> str:
    """
    Deletes a file from the current directory.


    Args:
        filename: The name of the file to delete.


    Returns:
        A message confirming success or describing the error.
    """

    try:
        if not os.path.isfile(filename):
            return f"Error: File '{filename}' does not exist."
        
        os.remove(filename)
        return f"Successfully deleted file: '{os.path.abspath(filename)}'."

    except Exception as e:
        return f"Error deleting file '{filename}': {e}"


def delete_folder(folder_name: str) -> str:
    """
    Deletes a folder from the current directory (only if it is empty).


    Args:
        folder_name: The folder to delete.


    Returns:
        A message confirming success or describing the error.
    """
    
    try:
        if not os.path.isdir(folder_name):
            return f"Error: Folder '{folder_name}' does not exist."
        
        os.rmdir(folder_name)  # Only deletes empty folders
        return f"Successfully deleted folder: '{os.path.abspath(folder_name)}'."

    except Exception as e:
        return f"Error deleting folder '{folder_name}': {e}"


def list_all_files(folder_path: str) -> str:
    """
    Lists all files and folders in the specified folder path.

    Args:
        folder_path: The path of the folder to list (e.g., './' for current directory).

    Returns:
        A formatted string containing all entries or an error message.
    """
    
    try:
        items = os.listdir(folder_path)
        
        if not items:
            return f"The folder '{folder_path}' is empty."



        result = f"Contents of folder '{folder_path}':\n"
        for name in items:
            path = os.path.abspath(os.path.join(folder_path, name))
            if os.path.isdir(path):
                result += f"[DIR]  {path}\n"
            else:
                result += f"[FILE] {path}\n"
        
        return result.strip()

    except Exception as e:
        return f"Error listing directory contents: {e}"
   
# file creation and writing
def write_file(filename: str, content: str) -> str:
    """
    Writes content to a file, creating it if it doesn't exist or overwriting if it does.

    Args:
        filename: The name of the file to write to.
        content: The string content to write into the file.

    Returns:
        A message confirming the file was written successfully or describing any error.
    """
    
    with open(filename, "w") as f:
        f.write(content)
    return f"File '{filename}' written successfully."

def append_to_file(filename: str, content: str) -> str:
    """
    Appends content to an existing file or creates a new file if it doesn't exist.

    Args:
        filename: The name of the file to append to.
        content: The string content to append to the file.

    Returns:
        A message confirming the content was appended successfully or describing any error.
    """
    
    with open(filename, "a") as f:
        f.write(content)
    return f"Content appended to file '{filename}' successfully."

def overwrite_file(filename: str, content: str) -> str:
    """
    Overwrites the content of a file, creating it if it doesn't exist.
    
    Args:
        filename: The name of the file to overwrite.
        content: The string content to write into the file. 
    
    Returns:
        A message confirming the file was overwritten successfully or describing any error.
    """
    
    return write_file(filename, content)

def create_file_with_content(filename: str, content: str) -> str:
    """
    Creates a new file with the specified content. If the file already exists, it will be overwritten.

    Args:
        filename: The name of the file to create.
        content: The string content to write into the file.

    Returns:
        A message confirming the file was created successfully or describing any error.
    """
    
    return write_file(filename, content)

# file reading
def read_file(filename: str) -> str:
    """
    Reads the entire content of a file.

    Args:
        filename: The name of the file to read.

    Returns:
        The content of the file or an error message.
    """
    
    try:
        with open(filename, "r") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file '{filename}': {e}"

def read_head(filename: str, n: int) -> str:
    """
    Reads the first n lines of a file.

    Args:
        filename: The name of the file to read.
        n: The number of lines to read from the beginning of the file.

    Returns:
        The first n lines of the file or an error message.
    """
    
    try:
        with open(filename, "r") as f:
            lines = [next(f) for _ in range(n)]
            return "".join(lines)
    except Exception as e:
        return f"Error reading head of file '{filename}': {e}"

def read_tail(filename: str, n: int) -> str:
    """
    Reads the last n lines of a file.

    Args:
        filename: The name of the file to read.
        n: The number of lines to read from the end of the file.

    Returns:
        The last n lines of the file or an error message.
    """
    
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            return "".join(lines[-n:])
    except Exception as e:
        return f"Error reading tail of file '{filename}': {e}"

def read_file_by_line(filename: str, line_number: int) -> str:
    """
    Reads a specific line from a file and returns it.

    Args:
        filename: The name of the file to read.
        line_number: The line number to read (1-indexed).

    Returns:
        The content of the specified line or an error message.
    """
    
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            if 1 <= line_number <= len(lines):
                return lines[line_number - 1].strip()
            else:
                return f"Line {line_number} is out of bounds for file '{filename}'."
    except Exception as e:
        return f"Error reading file '{filename}': {e}"

def read_file_with_line_numbers(filename: str) -> str:
    """
    Reads a file and returns its content formatted with line numbers.

    Args:
        filename: The name of the file to read.

    Returns:
        The content of the file formatted with line numbers or an error message.
    """
    
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
        return "\n".join(f"{i+1}: {line}" for i, line in enumerate(lines))
    except Exception as e:
        return f"Error reading file '{filename}': {e}"

# copy and move
def copy_file(src: str, dst: str) -> str:
    """
    Copies a file from the source path to the destination path.

    Args:
       src: The path of the source file to copy.
       dst: The path of the destination where the file should be copied.

    Returns:
        A message confirming the file was copied successfully or describing any error.
    """ 

    try:
        if not os.path.isfile(src):
            return f"Error: Source file '{src}' does not exist."
        
        with open(src, "rb") as f_src:
            content = f_src.read()
        with open(dst, "wb") as f_dst:
            f_dst.write(content)
        return f"File copied successfully from '{src}' to '{dst}'."
    except Exception as e:
        return f"Error copying file from '{src}' to '{dst}': {e}"

def move_file(src: str, dst: str) -> str:
    """
    Moves a file from the source path to the destination path.

    Args:
       src: The path of the source file to move.
       dst: The path of the destination where the file should be moved.
    Returns:
        A message confirming the file was moved successfully or describing any error.
    """
    
    try:
        if not os.path.isfile(src):
            return f"Error: Source file '{src}' does not exist."
        
        os.rename(src, dst)
        return f"File moved successfully from '{src}' to '{dst}'."
    except Exception as e:
        return f"Error moving file from '{src}' to '{dst}': {e}"

def rename_file(old_name: str, new_name: str) -> str:
    """
    Renames a file from the old name to the new name.

    Args:
        old_name: The current name of the file.
        new_name: The desired name for the file.

    Returns:
        A message confirming the file was renamed successfully or describing any error.
    """
    
    try:
        if not os.path.isfile(old_name):
            return f"Error: File '{old_name}' does not exist."
        
        os.rename(old_name, new_name)
        return f"File renamed successfully from '{old_name}' to '{new_name}'."
    except Exception as e:
        return f"Error renaming file from '{old_name}' to '{new_name}': {e}"

def modify_file(filepath: str, new_content: str) -> str:
    """
    Overwrites a file with modified content.

    Args:
        filepath: Path of file to modify
        new_content: Full updated content of the file

    Returns:
        Success or error message
    """

    try:
        if not os.path.isfile(filepath):
            return f"Error: File '{filepath}' does not exist."

        with open(filepath, "w") as f:
            f.write(new_content)

        return f"Successfully updated file: {os.path.abspath(filepath)}"

    except Exception as e:
        return f"Error modifying file '{filepath}': {e}"