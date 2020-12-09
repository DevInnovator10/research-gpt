# utils.py
import json
import re
from openai import OpenAI

from decouple import config

api = config("OPENAI_API_KEY")
client = OpenAI(api_key=api)

def get_gpt_response(messages, model="gpt-4o-2024-11-20", return_json=False):
    """Validate input."""
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    reply = response.choices[0].message.content.strip()

    if not return_json:
        return reply

    # Try parsing JSON content from GPT output
    try:
        return json.loads(reply)
    except json.JSONDecodeError:
        match = re.search(r'\{[\s\S]*\}', reply)
        if match:

            return json.loads(match.group(0))
        raise ValueError("No valid JSON found in GPT response")
