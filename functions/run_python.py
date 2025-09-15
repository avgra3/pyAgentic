from pathlib import Path
from subprocess import run, CalledProcessError


def run_python_file(working_directory, file_path, args=[]):
    path_to_check = Path(working_directory).absolute() / file_path
    if not str(path_to_check.resolve()).startswith(
        str(Path(working_directory).absolute())
    ):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not path_to_check.exists():
        return f'Error: File "{file_path}" not found.'
    if not path_to_check.as_posix().endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    err = ""
    try:
        output = run(
            ["uv", "run", file_path, *args],
            cwd=working_directory,
            timeout=30,
            capture_output=True,
        )
    except CalledProcessError as e:
        err = f"Process exited with code {e.returncode}"
    if output.stderr == "" and output.stdout == "" and err == "":
        return "No output produced"
    outmessage = f"STDOUT: {output.stdout}" + "\n" + f"STDERR: {output.stderr}"
    if len(err) > 0:
        outmessage += "\n" + err
    return outmessage
