import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
import argparse
from functions.get_files_info import available_functions
from functions.call_function import call_function


class NotEnoughArgs(Exception):
    def __init__(self, message: str, error_code):
        super().__init__(message)
        self.error_code = error_code


def run_ai(input: str, api_key: str, verbose: bool, system_prompt: str):
    client = genai.Client(api_key=api_key)
    if input is None:
        raise NotEnoughArgs(message="No provided prompt.", error_code=1)
    messages = [types.Content(role="user", parts=[types.Part(text=input)])]
    generated_content = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    meta_data = generated_content.usage_metadata
    if verbose:
        print(f"User prompt: {input}")
        print(f"Prompt tokens: {meta_data.prompt_token_count}")
        print(f"Response tokens: {meta_data.candidates_token_count}")
    # print(generated_content.text)
    function_calls = generated_content.function_calls
    if len(function_calls) > 0:
        for function_call_part in function_calls:
            print(
                f"Calling function: {function_call_part.name}({function_call_part.args})"
            )
            result = call_function(
                function_call_part=function_call_part, verbose=verbose
            )
            response = result.parts[0].function_response.response
            if response is None:
                sys.exit("Error: No function response")
            if verbose:
                print(f"-> {response}")


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    system_prompt = os.environ.get("SYSTEM_PROMPT")
    parser = argparse.ArgumentParser(
        prog="pyAgentic",
        description="AI agent written in Python",
    )
    parser.add_argument("input")
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()
    run_ai(
        input=args.input,
        api_key=api_key,
        verbose=args.verbose,
        system_prompt=system_prompt,
    )


if __name__ == "__main__":
    main()
