import os
from dotenv import load_dotenv, find_dotenv

from google import genai

from magnetar_deer.agent.instructions import instructions

#TODO: Move .env file to ROOT and update dotenv accordingly
load_dotenv(".env")
# api_key = os.getenv("GEMINI_API_KEY")

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

chats = []

while True:
    user_input = input('$ ')
    if user_input == 'exit':
        break
    history = f"${instructions} ${chats}, Current prompt: ${user_input}"
    response = client.models.generate_content(
        model="gemini-3-flash-preview", 
        contents=history
    )
    chats.append({"prompt": user_input, "agent": response.text})
    print(response.text)

print(chats)