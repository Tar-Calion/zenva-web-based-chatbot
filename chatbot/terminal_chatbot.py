from model_client.llm_chat import LLMChat
from enum import Enum


class Starter(Enum):
    USER = 1
    MODEL = 2


class Terminal_Chatbot:
    exit_command = "q"

    def start_chat(self, chat: LLMChat, starter: Starter = Starter.USER):

        print(f"Chatbot is ready to chat with you. Type '{self.exit_command}' to close the chat.")

        if starter == Starter.MODEL:
            response = chat.send_message(None)
            print(f">>> Bot ({response.history_count} messages, {response.history_size} bytes): \n{response.text}")

        while True:
            user_input = input(">>> You: ")
            if user_input.lower() == self.exit_command:
                break

            response = chat.send_message(user_input)
            print(f">>> Bot ({response.history_count} messages, {response.history_size} bytes): \n{response.text}")
