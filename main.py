
from chatbot.chatbot import Chatbot
from model_client.gemini_pro_chat import GeminiProChat
from model_client.openai_chat import OpenAIChat


# chat_client = GeminiProChat()
chat_client = OpenAIChat()

chatbot = Chatbot()
chatbot.start_chat(chat_client)
