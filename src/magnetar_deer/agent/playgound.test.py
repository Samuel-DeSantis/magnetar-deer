import os
from dotenv import load_dotenv

from google import genai

#TODO: Move .env file to ROOT and update dotenv accordingly
load_dotenv("agent.env")
api_key = os.getenv("GEMINI_API_KEY")

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
)
print(response.text)