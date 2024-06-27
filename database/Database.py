import mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hotel_durbar"
        )
        self.cursor = self.connection.cursor()

    def get_user(self, username, password):
        query = '''SELECT user_id, username, user_type, user_status, full_name
                   FROM user WHERE username=%s AND password=%s'''
        self.cursor.execute(query, (username, password))
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.connection.close()
