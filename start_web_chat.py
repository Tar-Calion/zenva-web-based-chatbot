import gradio as gr
from model_client.chat_factory import create_chat_client

chat_client = create_chat_client()


def respond(new_message, history):
    print(f">>> You: {new_message}")

    response = chat_client.send_message(new_message)

    print(f">>> Bot ({response.history_count} messages, {response.history_size} bytes): \n{response.text}")

    return response.text


gr.ChatInterface(respond).launch()
