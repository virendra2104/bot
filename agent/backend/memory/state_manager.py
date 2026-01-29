class AgentState:
    def __init__(self):
        self.data = {}

    def set(self, key, value):
        self.data[key] = value

    def get(self, key, default=None):
        return self.data.get(key, default)

    def has(self, key):
        return key in self.data

    def clear(self, key=None):
        if key:
            self.data.pop(key, None)
        else:
            self.data = {}

    # Short-term memory for recent user message
    def set_last_message(self, message: str):
        self.data["last_message"] = message

    def get_last_message(self):
        return self.data.get("last_message")

    def clear_last_message(self):
        self.data.pop("last_message", None)
