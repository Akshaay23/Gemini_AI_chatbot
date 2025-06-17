import os
from dotenv import load_dotenv
import chainlit as cl
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

@cl.on_message
async def message_handler(message: cl.Message):
    user_input = message.content
    response = model.generate_content(user_input)
    await cl.Message(content=response.text).send()

