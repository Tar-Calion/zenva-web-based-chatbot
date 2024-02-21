class ChatResponse:
    def __init__(self, text: str, history_count: int, history_size: int):
        self.text = text
        self.history_count = history_count
        self.history_size = history_size
