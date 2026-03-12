import subprocess

def run_python_file(filepath):
    """
    Runs a Python file and returns its output.
    Args:
        filepath: The path of the file to run (e.g., './run.py').
    Returns:
        A message containing the output of code.
    """
    try:
        result = subprocess.run(['python', filepath], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error running file: {e.stderr}"
    except FileNotFoundError:
        return "Error: Python interpreter not found."
