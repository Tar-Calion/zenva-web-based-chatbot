
from chatbot.terminal_chatbot import Terminal_Chatbot, Starter
from model_client.chat_factory import create_chat_client


chat_client = create_chat_client()

chatbot = Terminal_Chatbot()
chatbot.start_chat(chat_client, starter=Starter.USER)
