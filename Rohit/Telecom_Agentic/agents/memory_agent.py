import json

class MemoryAgent:

    MEMORY_FILE = "memory/conversation_memory.json"

    def save_conversation(self, user_query, response):

        data = {
            "query": user_query,
            "response": response
        }

        try:
            with open(self.MEMORY_FILE, "r") as file:
                conversations = json.load(file)

        except:
            conversations = []

        conversations.append(data)

        with open(self.MEMORY_FILE, "w") as file:
            json.dump(conversations, file, indent=4)
