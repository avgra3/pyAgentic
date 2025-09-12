from pathlib import Path
import os
from .config import MAX_CHARACTER_LENGTH


def get_files_info(working_directory, directory="."):
    # directory => relative path param within working directory
    path_to_check = Path(working_directory).absolute() / directory
    if not path_to_check.exists() or not str(path_to_check.resolve()).startswith(
        str(Path(working_directory).absolute())
    ):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not path_to_check.is_dir():
        return f'Error "{directory}" is not a directory'
    for file in path_to_check.iterdir():
        try:
            return f"- {file.name}: file_size={os.path.getsize(file.absolute())} bytes, is_dir={file.is_dir()}"
        except FileNotFoundError:
            return f'Error: "{file}" does not exist'


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
