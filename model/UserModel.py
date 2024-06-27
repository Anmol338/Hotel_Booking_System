from database import Database

class UserModel:
    def __init__(self):
        self.db = Database.Database()

    def validate_user(self, username, password):
        user = self.db.get_user(username, password)
        return user

    def close_connection(self):
        self.db.close()
