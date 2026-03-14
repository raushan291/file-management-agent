import subprocess
import os

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

def run_shell_command(command: str, timeout: int = 10) -> dict:
    """
    Runs a shell command.

    If the command finishes within `timeout` seconds, return its output.
    If it exceeds timeout, treat it as a long-running process and run it in background.
    """

    try:
        # Try running normally first
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout
        )

        return {
            "output": result.stdout.strip(),
            "error": result.stderr.strip(),
            "returncode": result.returncode,
            "isError": result.returncode != 0
        }

    except subprocess.TimeoutExpired:
        # Command is likely long-running -> run in background
        try:
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            return {
                "output": f"Command started in background (PID: {process.pid})",
                "error": "",
                "returncode": None,
                "isError": False
            }

        except Exception as e:
            return {
                "output": "",
                "error": f"Failed to start background process: {str(e)}",
                "returncode": 1,
                "isError": True
            }

    except Exception as e:
        return {
            "output": "",
            "error": str(e),
            "returncode": 1,
            "isError": True
        }

def stop_process(pid: int) -> dict:
    """
    Stops a running process given its PID.
    Args:
        pid: The process ID to stop.
    Returns:
        A message indicating success or failure.
    """
    try:
        os.kill(pid, 9) # SIGKILL to forcefully terminate
        return {
            "output": f"Process {pid} terminated successfully.",
            "error": "",
            "returncode": 0,
            "isError": False
        }
    except ProcessLookupError:
        return {
            "output": "",
            "error": f"Process with PID {pid} not found.",
            "returncode": 1,
            "isError": True
        }
    except Exception as e:
        return {
            "output": "",
            "error": str(e),
            "returncode": 1,
            "isError": True
        }
