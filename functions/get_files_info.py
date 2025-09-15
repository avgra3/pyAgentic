from pathlib import Path
import os
from .config import MAX_CHARACTER_LENGTH
from google.genai import types
from .run_python import run_python_file
from .write_file import write_file


def get_files_info(working_directory, directory="."):
    # directory => relative path param within working directory
    path_to_check = Path(working_directory).absolute() / directory
    if not path_to_check.exists() or not str(path_to_check.resolve()).startswith(
        str(Path(working_directory).absolute())
    ):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not path_to_check.is_dir():
        return f'Error "{directory}" is not a directory'
    output = ""
    for file in path_to_check.iterdir():
        try:
            output += f"- {file.name}: file_size={os.path.getsize(file.absolute())} bytes, is_dir={file.is_dir()}\n"
        except FileNotFoundError:
            return f'Error: "{file}" does not exist'
    return output


def get_file_content(working_directory, file_path):
    working_directory = Path(working_directory)
    file_path = working_directory / Path(file_path)
    if not str(file_path.resolve()).startswith(str(working_directory.absolute())):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not file_path.is_file():
        return f'Error: File not found or is not a regular file: "{file_path}"'
    with open(file_path, "r") as file:
        all_data = file.read(MAX_CHARACTER_LENGTH + 1)
        if len(all_data) > MAX_CHARACTER_LENGTH:
            all_data = (
                all_data[:MAX_CHARACTER_LENGTH]
                + f'[...File "{file_path}" truncated at {MAX_CHARACTER_LENGTH} characters]'
            )
    return all_data


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Get the content from a specified file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file that we want to get the content of. If no file is provided, return an empty string",
            ),
        },
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run the specified python file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Run the specified python file",
            ),
        },
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write to the specified file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File to write to",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content you would like to write to the specified file",
            ),
        },
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)
