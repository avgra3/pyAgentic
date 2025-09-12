from pathlib import Path
import os


def get_files_info(working_directory, directory="."):
    # directory => relative path param within working directory
    path_to_check = Path(working_directory).absolute() / directory
    if not path_to_check.exists() or not str(path_to_check.resolve()).startswith(
        str(Path(working_directory).absolute())
    ):
        print(
            f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        )
        return
    if not path_to_check.is_dir():
        print(f'Error "{directory}" is not a directory')
        return
    for file in path_to_check.iterdir():
        try:
            print(
                f"- {file.name}: file_size={os.path.getsize(file.absolute())} bytes, is_dir={file.is_dir()}"
            )
        except FileNotFoundError:
            print(f'Error: "{file}" does not exist')
