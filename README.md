# zenva-web-based-chatbot
Allows users to chat with OpenAI's GPT-3.5 or Google Palm Pro LLMs.

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

To start the chatbot, run the following command:
```
python start_chat.py
```

To start the quiz chatbot, run the following command:
```
python start_quiz.py
```

