from vertexai.preview.generative_models import GenerativeModel
from model_client.llm_chat import LLMChat
from model_client.chat_response import ChatResponse


class GeminiProChat(LLMChat):
    """Client for interacting with the Gemini Pro model."""

    def __init__(self, system_prompt: str = None):
        self.model = GenerativeModel("gemini-1.0-pro-001")
        self.system_prompt = system_prompt

        self.chat = self.model.start_chat()

    def __calculate_history_size(self) -> int:
        return sum(len(content.parts[0].text) for content in self.chat.history)

    def send_message(self, prompt: str) -> ChatResponse:
        """Send a message to the model and return its response."""

        # add system prompt if this is the first message
        if len(self.chat.history) == 0 and self.system_prompt:
            prefix = "Instructions: " + self.system_prompt
            if prompt == None:
                prompt = prefix
            else:
                prompt = prefix + "\n" + "User: " + prompt

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
