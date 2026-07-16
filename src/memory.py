"""
Conversation Memory
"""

from collections import deque

from src.config import MAX_HISTORY


class ConversationMemory:

    def __init__(self):
        self.history = deque(maxlen=MAX_HISTORY)

    def add(self, role, message):
        self.history.append({
            "role": role,
            "message": message
        })

    def get_context(self):

        conversation = ""

        for chat in self.history:

            conversation += (
                f"{chat['role']}: {chat['message']}\n"
            )

        return conversation

    def clear(self):
        self.history.clear()