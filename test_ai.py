import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

print(f"API Key loaded: {api_key[:10]}...{api_key[-5:] if api_key else 'None'}")

if not api_key:
    print("Error: No API Key found.")
    exit()

client = OpenAI(api_key=api_key)

try:
    print("Attempting to connect to OpenAI...")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Say hello in JSON format: {'msg': 'hello'}"}
        ],
    )
    print("Success!")
    print(response.choices[0].message.content)
except Exception as e:
    print("FAILED!")
    print(e)
