from google.genai import types
from .get_files_info import get_files_info, get_file_content
from .write_file import write_file
from .run_python import run_python_file


def call_function(
    function_call_part: types.FunctionCall, verbose: bool = False
) -> types.Content:
    name = function_call_part.name
    args = function_call_part.args
    funcs = function_names(name=name)
    if verbose:
        print(f"Calling function: {name}({args})")
    else:
        print(f" - Calling function: {name}")
    args["working_directory"] = "./calculator"
    try:
        result = funcs(**args)
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=name,
                    response={"result": result},
                )
            ],
        )
    except:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=name,
                    response={"error": f"Unknown function: {name}"},
                )
            ],
        )


def function_names(name: str) -> callable:
    function_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "write_file": write_file,
        "run_python_file": run_python_file,
    }
    try:
        returned = function_map[name]
        return returned
    except:
        print(f"function name '{name}' unknown")
        return None
