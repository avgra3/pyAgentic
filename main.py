import os
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    base_prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    generated_content = client.models.generate_content(
        model="gemini-2.0-flash-001", contents=base_prompt
    )
    meta_data = generated_content.usage_metadata
    print(generated_content.text)
    print(f"Prompt tokens: {meta_data.prompt_token_count}")
    print(f"Response tokens: {meta_data.candidates_token_count}")


if __name__ == "__main__":
    main()
