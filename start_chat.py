
from chatbot.chatbot import Chatbot, Starter
from model_client.chat_factory import create_chat_client


chat_client = create_chat_client()

chatbot = Chatbot()
chatbot.start_chat(chat_client, starter=Starter.USER)
