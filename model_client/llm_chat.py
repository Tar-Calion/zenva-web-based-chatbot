from model_client.chat_response import ChatResponse


class LLMChat:
    """Interface for interacting with a generative model."""

    def send_message(self, prompt: str) -> ChatResponse:
        """Send a message to the model and return its response."""
        pass
