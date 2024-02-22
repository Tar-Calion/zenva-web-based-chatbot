# zenva-web-based-chatbot
Allows users to chat with OpenAI's GPT-3.5 or Google Palm Pro LLMs. The chatbot can be used in a web-based chat or in a terminal chat.

## Installation
Create `.env` file in the root directory of the project and set the model you want to use. Allowed values are "GEMINI-PRO" and "GPT-3.5". The file should look like this:

```
LLM_MODEL="GEMINI-PRO"

OPENAI_API_KEY="sk-xxx"
```

See ``example.env`` for an example.

In order to be able to use OpenAI API, you also need to put your API key in the `.env` file.

If you want to use Google's Palm Pro instead, you need to log in to Google Cloud via `gcloud auth application-default login`.


## Usage

Starter scripts for terminal chats:
- `start_terminal_chat.py`
- `start_terminal_quiz.py`

After starting the terminal chat, you can chat with the chatbot in the terminal.

Starter scripts for web-based chats:
- `start_web_chat.py`
- `start_web_quiz.py`

After starting the web-based chat, you can access the chatbot at `http://127.0.0.1:7860`.

