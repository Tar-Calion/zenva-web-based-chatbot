from model_client.llm_chat import LLMChat
from enum import Enum


class Starter(Enum):
    USER = 1
    MODEL = 2

class Chatbot:

    def start_chat(self, chat: LLMChat, starter: Starter = Starter.USER):

        print("Chatbot is ready to chat with you. Type 'exit' to close the chat.")

        if starter == Starter.MODEL:
            response = chat.send_message(None)
            print(f"Bot ({response.history_count} messages, {response.history_size} bytes): \n{response.text}")

        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                break

            response = chat.send_message(user_input)
            print(f"Bot ({response.history_count} messages, {response.history_size} bytes): \n{response.text}")
