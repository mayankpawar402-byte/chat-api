import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


def get_ai_response(message: str):

    response = client.chat.completions.create(
        model="nvidia/nemotron-3-super-120b-a12b:free",
        messages=[
            {
                "role": "system",
                "content": "You are ICEBEAR Assistant. Explain things clearly and simply."
            },
            {
                "role": "user",
                "content": message
            }
        ]
    )

    return response.choices[0].message.content