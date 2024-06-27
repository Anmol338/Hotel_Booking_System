# login.py
from tkinter import Tk, Frame, Label, TOP, Entry, ttk, LEFT, Button, RIGHT
from tkinter.font import BOLD
from controller import UserController

class LogIn_window:
    def __init__(self, window):
        self.window = window
        self.window.title('Hotel Management System')
        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        window.geometry(f'{width}x{height}+0+0')
        self.window.configure(background='#000000')
        self.window.wm_state('zoomed')
        heading_lbl = Label(self.window, text='Hotel Management System', font=('Times New Roman', 40, BOLD), bg='#000000', fg='#ffffff')
        heading_lbl.pack(side=TOP, pady=20)
        self.sign_In_form()
        self.controller = UserController.UserController()  # Initialize UserController

    def sign_In_form(self):
        frame = Frame(self.window, bg='white', width=600, height=500)
        frame.place(x=450, y=200)
        heading_logIn = Label(frame, text='LogIn', bg='white', fg='#000000', font=('Times New Roman', 30, BOLD))
        heading_logIn.place(x=250, y=20)

        def on_click_user(e):
            if self.username_entry.get() == 'Username':
                self.username_entry.delete(0, 'end')

        def on_leave_user(e):
            if self.username_entry.get() == '':
                self.username_entry.insert(0, 'Username')

        def on_click_pass(e):
            if self.password_entry.get() == 'Password':
                self.password_entry.delete(0, 'end')

        def on_leave_pass(e):
            if self.password_entry.get() == '':
                self.password_entry.insert(0, 'Password')

        self.username_entry = Entry(frame, width=36, border=0, font=('Times New Roman', 20, BOLD))
        self.username_entry.place(x=50, y=150)
        Frame(frame, width=500, height=2, bg='black').place(x=50, y=185)
        self.username_entry.insert(0, 'Username')
        self.username_entry.bind('<FocusIn>', on_click_user)
        self.username_entry.bind('<FocusOut>', on_leave_user)

        self.password_entry = Entry(frame, width=36, border=0, font=('Times New Roman', 20, BOLD), show='*')
        self.password_entry.place(x=50, y=250)
        Frame(frame, width=500, height=2, bg='black').place(x=50, y=285)
        self.password_entry.insert(0, 'Password')
        self.password_entry.bind('<FocusIn>', on_click_pass)
        self.password_entry.bind('<FocusOut>', on_leave_pass)

        lbl_section = Label(frame, bg='white')
        lbl_section.place(x=50, y=310, width=500)
        ttk.Checkbutton(lbl_section, text="Show password", onvalue=True, offvalue=False, command=lambda: self.toggle_password()).pack(side=LEFT)
        Button(lbl_section, text='Forgot Password?', font=('Times New Roman', 14, BOLD), bg='white', border=0, cursor='hand2').pack(side=RIGHT)

        signIn_btn = Button(frame, width=42, pady=2, text='SignIn', bg='black', fg='white', border=0, cursor='hand2',
                            font=('Times New Roman', 16, BOLD), command=lambda: self.controller.validate_login(self.username_entry.get(), self.password_entry.get(), self.window))
        signIn_btn.place(x=50, y=380)

        signUp_txt_lbl = Label(frame, text="Not Yet Member?", fg='black', bg='white', font=('Times New Roman', 12, BOLD))
        signUp_txt_lbl.place(x=200, y=450)
        signUp_btn = Button(frame, width=8, text='Registration', border=0, bg='white', cursor='hand2', fg='#57a1f8', font=('Times New Roman', 12, BOLD), command=lambda: self.close())
        signUp_btn.place(x=340, y=450)

    def close(self):
        self.window.destroy()
        self.new_obj = Tk()
        # Registration_Gui.Registration(self.new_obj)

    def toggle_password(self):
        if self.password_entry.cget('show') == '*':
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')

if __name__ == '__main__':
    obj = Tk()
    ui = LogIn_window(obj)
    obj.mainloop()
