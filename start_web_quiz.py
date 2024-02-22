import gradio as gr
from model_client.chat_factory import create_chat_client
from start_terminal_quiz import system_prompt

chat_client = create_chat_client(system_prompt)
first_response = chat_client.send_message(None)


def respond(new_message, history):
    print(f">>> You: {new_message}")

    response = chat_client.send_message(new_message)

    print(f">>> Bot ({response.history_count} messages, {response.history_size} bytes): \n{response.text}")

    return response.text


chatbot = gr.Chatbot(value=[(None, first_response.text)])

gr.ChatInterface(respond, chatbot=chatbot).launch()
