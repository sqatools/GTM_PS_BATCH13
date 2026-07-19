class SessionMemory:

    def __init__(self):
        self.sessions = {}

    def save_session(self, session_id, data):
        self.sessions[session_id] = data

    def get_session(self, session_id):
        return self.sessions.get(session_id)
