
class SqlLiteSession:
    def __init__(self, session_id: str):
        self.session_id = session_id

    def get_history(self):
        #get the history from the DB
        pass

    def clear_history(self):
        #clear the history from the DB
        pass

    def update_history(self, history: list[dict[str, str]]):
        #update the history in the DB
        pass
    

class SQLiteSessionStore:
    def __init__(self):     
        pass

