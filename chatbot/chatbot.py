from model_client.llm_chat import LLMChat


class Chatbot:

    def start_chat(self, chat: LLMChat):

        print("Chatbot is ready to chat with you. Type 'exit' to close the chat.")

        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                break

            response = chat.send_message(user_input)

            print(f"Bot ({response.history_count} messages, {response.history_size} bytes): \n{response.text}")
