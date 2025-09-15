from pathlib import Path


def write_file(working_directory, file_path, content):
    path_to_check = Path(working_directory).absolute() / file_path
    if not str(path_to_check.resolve()).startswith(
        str(Path(working_directory).absolute())
    ):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not Path(file_path).exists():
        try:
            path_to_check.touch()
        except FileNotFoundError as e:
            return f"Error: {e}"
    with open(path_to_check, "w") as file:
        file.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
