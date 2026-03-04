from langchain_core.chat_history import InMemoryChatMessageHistory

class SessionManager():
    def __init__(self):
        self.store = {}
        self.sector_store = {}
    
    def session_history(self, session_id):
        if session_id not in self.store:
            self.store[session_id] = InMemoryChatMessageHistory()
        return self.store[session_id]

    def get_session_sector(self, session_id):
        return self.sector_store.get(session_id)
    
    def set_session_sector(self, session_id, sector):
        self.sector_store[session_id] = sector

manager = SessionManager()