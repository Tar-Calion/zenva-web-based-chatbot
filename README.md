# zenva-web-based-chatbot
Allows users to chat with OpenAI's GPT-3.5 or Google Palm Pro LLMs.

## Installation
In order to be able to use OpenAI API, you need to put your API key in the file `.env` in the root directory of the project. The file should look like this:
```
OPENAI_API_KEY=your-api-key
```

If you want to use Google's Palm Pro instead, you need to log in to Google Cloud via `gcloud auth application-default login`.


## Usage

In `main.py`, set the chat_client to either GeminiProChat or OpenAIChat:
```python
# chat_client = GeminiProChat()
# chat_client = OpenAIChat()

```

To start the chatbot, run the following command:
```
python main.py
```

