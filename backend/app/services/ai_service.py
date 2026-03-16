import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


def call_openrouter(prompt: str):

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(OPENROUTER_URL, json=payload, headers=headers)

    data = response.json()

    print("OPENROUTER RESPONSE:", data)

    return data["choices"][0]["message"]["content"]


def generate_task_details(title: str):

    prompt = prompt = prompt = f"""
        You are assisting a project management system so act as a project manager.

        Task Title: {title}

        Generate:

        1. A clear task description of the task title provided to you and the description you provided should explain the gist of title completely.
        2. A task priority based on the task title and task description you generate.

        Priority must be one of:
        Low
        Medium
        High

        IMPORTANT:
        Return ONLY valid JSON in this exact format.

        Example:
        {{
        "description": "task description",
        "priority": "Low"
        }}

        Do not add explanation or text outside JSON.
        """

    result = call_openrouter(prompt)

    return result