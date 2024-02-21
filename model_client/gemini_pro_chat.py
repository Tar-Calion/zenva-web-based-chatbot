from vertexai.preview.generative_models import GenerativeModel
from model_client.llm_chat import LLMChat
from model_client.chat_response import ChatResponse


class GeminiProChat(LLMChat):
    """Client for interacting with the Gemini Pro model."""

    def __init__(self):
        self.model = GenerativeModel("gemini-1.0-pro-001")
        self.chat = self.model.start_chat()

    def __calculate_history_size(self) -> int:
        return sum(len(content.parts[0].text) for content in self.chat.history)

    def send_message(self, prompt: str) -> str:
        """Send a message to the model and return its response."""
        if not prompt:
            raise ValueError("Prompt cannot be empty or None")

        config = {
            "max_output_tokens": 4000,
            "temperature": 0.9,
            "top_p": 1
        }

        response = self.chat.send_message(prompt, generation_config=config)

        response_text = response.candidates[0].content.parts[0].text

        history_count = len(self.chat.history)
        history_size = self.__calculate_history_size()

        return ChatResponse(response_text, history_count, history_size)
