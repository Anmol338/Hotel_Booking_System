# user_controller.py
from tkinter import messagebox
from model import UserModel
from views import dashboard  # Import the Dashboard class

class UserController:
    def __init__(self):
        self.model = UserModel.UserModel()

    def validate_login(self, username, password, login_window):
        if not username or username == 'Username':
            messagebox.showerror('Missing', 'Please fill in the username field!')
            return False
        elif not password or password == 'Password':
            messagebox.showerror('Missing', 'Please fill in the password field!')
            return False
        user = self.model.validate_user(username, password)
        if user:
            user_id, username, user_type, user_status, full_name = user
            messagebox.showinfo('Success', f'Login successful! Welcome {full_name}.')
            login_window.destroy()  # Close the login window
            dashboard.Dashboard()  # Open the Dashboard window
            return True
        else:
            messagebox.showerror('Error', 'Invalid username or password.')
            return False

    def close_connection(self):
        self.model.close_connection()
