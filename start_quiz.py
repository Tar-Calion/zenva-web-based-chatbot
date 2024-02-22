from chatbot.chatbot import Chatbot, Starter
from model_client.chat_factory import create_chat_client


system_prompt = """You are a Quiz Master. You are going to ask the user about a topic and generate multiple choice questions for them to answer.
When the user answers, you will tell them if they are correct and explain the correct answer. After that, you will ask the next question.
The topic is: The Python Programming Language, Advanced Questions. Generate the first question now."""

chat_client = create_chat_client(system_prompt)

chatbot = Chatbot()
chatbot.start_chat(chat_client, starter=Starter.MODEL)
