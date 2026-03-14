import tools

FILE_OPERATIONS = {
    "create_file": {
        "function": tools.create_file,
        "description": "Create a new empty file.",
        "parameters": {
            "type": "object",
            "properties": {
                "filename": {"type": "string"}
            },
            "required": ["filename"]
        }
    },

    "delete_file": {
        "function": tools.delete_file,
        "description": "Delete a file.",
        "parameters": {
            "type": "object",
            "properties": {
                "filename": {"type": "string"}
            },
            "required": ["filename"]
        }
    },

    "read_file": {
        "function": tools.read_file,
        "description": "Read contents of a file.",
        "parameters": {
            "type": "object",
            "properties": {
                "filename": {"type": "string"}
            },
            "required": ["filename"]
        }
    },

    "write_file": {
        "function": tools.write_file,
        "description": "Write content to a file (overwrite).",
        "parameters": {
            "type": "object",
            "properties": {
                "filename": {"type": "string"},
                "content": {"type": "string"}
            },
            "required": ["filename", "content"]
        }
    },

    "modify_file": {
        "function": tools.modify_file,
        "description": "Modify the content of a file by replacing it with new content.",
        "parameters": {
            "type": "object",
            "properties": {
                "filepath": {"type": "string"},
                "new_content": {"type": "string"}
            },
            "required": ["filepath", "new_content"]
        }
    }
}

DIRECTORY_OPERATIONS = {

    "create_folder": {
        "function": tools.create_folder,
        "description": "Create a new directory.",
        "parameters": {
            "type": "object",
            "properties": {
                "folder_name": {"type": "string"}
            },
            "required": ["folder_name"]
        }
    },

    "delete_folder": {
        "function": tools.delete_folder,
        "description": "Delete an empty directory.",
        "parameters": {
            "type": "object",
            "properties": {
                "folder_name": {"type": "string"}
            },
            "required": ["folder_name"]
        }
    },

    "list_files": {
        "function": tools.list_all_files,
        "description": "List files and directories in a folder.",
        "parameters": {
            "type": "object",
            "properties": {
                "folder_path": {"type": "string"}
            },
            "required": ["folder_path"]
        }
    }
}

SEARCH_OPERATIONS = {

    "search_file_by_name": {
        "function": tools.search_file_by_name,
        "description": "Search for files by name.",
        "parameters": {
            "type": "object",
            "properties": {
                "pattern": {"type": "string"},
                "folder_path": {"type": "string"}
            },
            "required": ["pattern", "folder_path"]
        }
    },

    "search_by_extension": {
        "function": tools.search_by_extension,
        "description": "Find files with a specific extension.",
        "parameters": {
            "type": "object",
            "properties": {
                "extension": {"type": "string"},
                "folder_path": {"type": "string"}
            },
            "required": ["extension", "folder_path"]
        }
    }
}

METADATA_OPERATIONS = {

    "get_file_info": {
        "function": tools.get_file_info,
        "description": "Get information about a file.",
        "parameters": {
            "type": "object",
            "properties": {
                "filename": {"type": "string"}
            },
            "required": ["filename"]
        }
    },

    "get_permissions": {
        "function": tools.get_permissions,
        "description": "Get permissions of a file.",
        "parameters": {
            "type": "object",
            "properties": {
                "path": {"type": "string"}
            },
            "required": ["path"]
        }
    },

    "file_exists": {
        "function": tools.file_exists,
        "description": "Check if a file exists.",
        "parameters": {
            "type": "object",
            "properties": {
                "filename": {"type": "string"}
            },
            "required": ["filename"]
        },
    },
}


ARCHIVE_OPERATIONS = {

    "zip_folder": {
        "function": tools.zip_folder,
        "description": "Compress a folder into a zip archive.",
        "parameters": {
            "type": "object",
            "properties": {
                "folder_path": {"type": "string"},
                "output_zip": {"type": "string"}
            },
            "required": ["folder_path", "output_zip"]
        }
    },

    "unzip_file": {
        "function": tools.unzip_file,
        "description": "Extract a zip file.",
        "parameters": {
            "type": "object",
            "properties": {
                "zip_path": {"type": "string"},
                "extract_to": {"type": "string"}
            },
            "required": ["zip_path", "extract_to"]
        }
    }
}

EXECUTE_OPERATIONS = {
    "run_python_file": {
        "function": tools.run_python_file,
        "description": "Runs a Python file and returns its output.",
        "parameters": {
            "type": "object",
            "properties": {
                "filepath": {"type": "string"}
            },
            "required": ["filepath"]
        }
    },
    
    "run_shell_command": {
        "function": tools.run_shell_command,
        "description": "Executes a shell command and returns its output.",
        "parameters": {
            "type": "object",
            "properties": {
                "command": {"type": "string"},
                "timeout": {"type": "integer", "description": "Timeout for the command in seconds."} 
            },
            "required": ["command"]
        }
    },
    
    "stop_process": {
        "function": tools.stop_process, 
        "description": "Stop a running process by its Process ID (PID).",
        "parameters": {
            "type": "object",
            "properties": {
                "pid": {"type": "string", "description": "The Process ID of the process to stop."}
            },
            "required": ["pid"]
        }
    }
}

TOOLS = {
    **FILE_OPERATIONS,
    **DIRECTORY_OPERATIONS,
    **SEARCH_OPERATIONS,
    **METADATA_OPERATIONS,
    **ARCHIVE_OPERATIONS,
    **EXECUTE_OPERATIONS,
}
