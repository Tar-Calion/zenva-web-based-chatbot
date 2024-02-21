from openai import OpenAI
from model_client.chat_response import ChatResponse
from model_client.llm_chat import LLMChat
import dotenv


class OpenAIChat(LLMChat):
    """Client for interacting with the OpenAI model."""

    def __init__(self):
        dotenv.load_dotenv(override=True)

        self.client = OpenAI()

        self.properties = {
            "model": "gpt-3.5-turbo-0125",
            "temperature": 1,
            "max_tokens": 2000,
        }

        self.messages = [
            {
                "role": "system",
                "content": "Your are a helpful assistant."
            }
        ]

    def send_message(self, prompt: str) -> ChatResponse:

        self.messages.append({
            "role": "user",
            "content": prompt
        })
        response = self.client.chat.completions.create(
            **self.properties,
            messages=self.messages
        )

        response_text = response.choices[0].message.content
        self.messages.append({
            "role": "assistant",
            "content": response_text
        })

        history_count = len(self.messages)
        history_size = self.__get_history_size()

        return ChatResponse(response_text, history_count, history_size)

    def __get_history_size(self):
        return sum([len(message["content"]) for message in self.messages])
