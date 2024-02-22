import os
import dotenv
from model_client.openai_chat import OpenAIChat
from model_client.llm_chat import LLMChat
from model_client.gemini_pro_chat import GeminiProChat


def create_chat_client(system_prompt=None) -> LLMChat:
    """Return the chat client to use."""

    dotenv.load_dotenv(override=True)

    model = os.getenv("LLM_MODEL")

    if model == "GPT-3.5":
        return OpenAIChat(system_prompt)
    elif model == "GEMINI-PRO":
        return GeminiProChat(system_prompt)
