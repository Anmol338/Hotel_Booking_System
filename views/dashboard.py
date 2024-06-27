from datetime import datetime
from tkinter import Tk, Frame, TOP, LEFT, BOTTOM, Label, Image, Button, W, messagebox, Entry, \
    LabelFrame, HORIZONTAL, VERTICAL, Scrollbar, END, N
from tkinter.font import BOLD
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from tkinter.ttk import Combobox, Treeview, Style

class Dashboard:
    def __init__(self):
        self.create()

    def create(self):
        self.window = Tk()
        # Defining Title of the window
        self.window.title('Admin Dashboard || Designed By Bikesh Prajapati')

        # Defining width and height of the window
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        self.window.geometry(f'{w}x{h}+0+0')
        self.window.wm_state('zoomed')
        self.window.wm_resizable(False, False)
        self.window.config(bg='#eff5f6')

        self.header_frame()
        self.left_side_frame()
        self.main_frame()

        self.window.mainloop()

    def header_frame(self):
        # Header Frame
        self.header_frame = Frame(self.window, width=1535, height=60, bg='#00FFAE')
        self.header_frame.pack(side=TOP)

        # Header label
        header_left_lbl = Label(self.header_frame, bg='#00FFAE', width=42, height=80)
        header_left_lbl.place(x=0, y=0)

        # Heading Label text
        heading_lbl_text = Label(header_left_lbl, text='Hotel Durbar', bg='#00FFAE', font=('Times New Roman', 18, BOLD),
                                 fg='#000000')
        heading_lbl_text.grid(row=1, column=0)

        # Heading Middle Text
        heading_md_lbl = Label(self.header_frame, text='Hotel Management System', font=('Times New Roman', 20, BOLD),
                               bg='#00FFAE', fg='#000000')
        heading_md_lbl.place(x=600, y=10)

    def main_frame(self):
        self.main_frame = Frame(self.window, width=1200, height=600, bg='#eff5f6')
        self.main_frame.place(x=320, y=150)


    ###### Left Side NavBar Design #####
    ##### ----- Function to define left side frame ----- #####
    def left_side_frame(self):
        # Left Side Frame design place
        self.left_side_frame = Frame(self.window, width=300, height=785, bg='#484D4B')
        self.left_side_frame.pack(side=LEFT, pady=(0, 0))

        ##### ----- Buttons ----- #####
        ##### ----- Make Booking Button Design
        self.make_booking_btn_lbl = Label(self.left_side_frame, width=300, height=4, bg='#484D4B')
        self.make_booking_btn_lbl.place(x=0, y=120)

        # Function to change properties of button while hovering the button
        def enter(event):
            self.make_booking_btn_lbl.configure(bg='#B316EE')
            self.make_booking_img_lbl.configure(bg='#B316EE')
            self.make_booking_btn.config(bg='#B316EE', fg='#000000')

        def leave(event):
            self.make_booking_btn_lbl.configure(bg='#484D4B')
            self.make_booking_img_lbl.configure(bg='#484D4B')
            self.make_booking_btn.config(bg='#484D4B', fg='#ffffff')

        ##### ----- Buttons ----- #####
        # Manage Booking Button Design
        self.make_booking_lbl = Label(self.make_booking_btn_lbl, width=300, height=4, bg='#484D4B')
        self.make_booking_lbl.place(x=0, y=0)
        self.make_booking_lbl.bind('<Enter>', enter)
        self.make_booking_lbl.bind('<Leave>', leave)

        # Manage Booking Image
        self.make_booking_img = Image.open('images/clipboard.png').resize((40, 40))
        self.make_booking_final_img = ImageTk.PhotoImage(self.make_booking_img)
        self.make_booking_img_lbl = Label(self.make_booking_lbl, image=self.make_booking_final_img, width=50,
                                          height=50, bg='#484D4B')
        self.make_booking_img_lbl.place(x=5, y=0)

        # Manage Booking Button
        self.make_booking_btn = Button(self.make_booking_lbl, text='Manage Booking', font=('Times New Roman', 20, BOLD),
                                       bg='#484D4B', fg='#ffffff', cursor='hand2', width=14, bd=0, anchor=W,
                                       activebackground='#B316EE')
        self.make_booking_btn.place(x=60, y=5)


        ##### ----- Manage Service Button Design ----- #####
        #####################################################
        self.service_btn_lbl = Label(self.left_side_frame, width=300, height=4, bg='#484D4B')
        self.service_btn_lbl.place(x=0, y=220)

        # Function to change properties of button while hovering the button
        def enter(event):
            self.service_lbl.configure(bg='#B316EE')
            self.service_img_lbl.configure(bg='#B316EE')
            self.service_btn.config(bg='#B316EE', fg='#000000')

        def leave(event):
            self.service_lbl.configure(bg='#484D4B')
            self.service_img_lbl.configure(bg='#484D4B')
            self.service_btn.config(bg='#484D4B', fg='#ffffff')

        ##### ----- Buttons ----- #####
        # Manage Booking Button Design
        self.service_lbl = Label(self.service_btn_lbl, width=300, height=4, bg='#484D4B')
        self.service_lbl.place(x=0, y=0)
        self.service_lbl.bind('<Enter>', enter)
        self.service_lbl.bind('<Leave>', leave)

        # Booking History Image
        self.service_img = Image.open('images/clock.png').resize((40, 40))
        self.service_final_img = ImageTk.PhotoImage(self.service_img)
        self.service_img_lbl = Label(self.service_lbl, image=self.service_final_img,
                                             width=50, height=50,
                                             bg='#484D4B')
        self.service_img_lbl.place(x=5, y=0)

        # Booking History Button
        self.service_btn = Button(self.service_lbl, text='Manage Service',
                                          font=('Times New Roman', 20, BOLD),
                                          bg='#484D4B', fg='#ffffff', cursor='hand2', width=14, bd=0, anchor=W,
                                          activebackground='#B316EE')
        self.service_btn.place(x=60, y=5)

        ##### ----- Customer Button Design
        self.customer_btn_lbl = Label(self.left_side_frame, width=300, height=4, bg='#484D4B')
        self.customer_btn_lbl.place(x=0, y=320)

        # Function to change properties of button while hovering the button
        def enter(event):
            self.customer_lbl.configure(bg='#B316EE')
            self.customer_img_lbl.configure(bg='#B316EE')
            self.customer_btn.config(bg='#B316EE', fg='#000000')

        def leave(event):
            self.customer_lbl.configure(bg='#484D4B')
            self.customer_img_lbl.configure(bg='#484D4B')
            self.customer_btn.config(bg='#484D4B', fg='#ffffff')

        ##### ----- Buttons ----- #####
        # Manage Booking Button Design
        self.customer_lbl = Label(self.customer_btn_lbl, width=300, height=4, bg='#484D4B')
        self.customer_lbl.place(x=0, y=0)
        self.customer_lbl.bind('<Enter>', enter)
        self.customer_lbl.bind('<Leave>', leave)

        # Customer Image
        self.customer_img = Image.open('images/crm.png').resize((40, 40))
        self.customer_final_img = ImageTk.PhotoImage(self.customer_img)
        self.customer_img_lbl = Label(self.customer_lbl, image=self.customer_final_img, width=50, height=50,
                                      bg='#484D4B')
        self.customer_img_lbl.place(x=5, y=0)

        # Customer Button
        self.customer_btn = Button(self.customer_lbl, text='Manage Customer',
                                   font=('Times New Roman', 20, BOLD),
                                   bg='#484D4B', fg='#ffffff', cursor='hand2', width=14, bd=0, anchor=W,
                                   activebackground='#B316EE')
        self.customer_btn.place(x=60, y=5)

        ##### ----- Driver Button Design
        self.room_btn_lbl = Label(self.left_side_frame, width=300, height=4, bg='#484D4B')
        self.room_btn_lbl.place(x=0, y=420)

        # Function to change properties of button while hovering the button
        def enter(event):
            self.room_lbl.configure(bg='#B316EE')
            self.room_img_lbl.configure(bg='#B316EE')
            self.room_btn.config(bg='#B316EE', fg='#000000')

        def leave(event):
            self.room_lbl.configure(bg='#484D4B')
            self.room_img_lbl.configure(bg='#484D4B')
            self.room_btn.config(bg='#484D4B', fg='#ffffff')

        ##### ----- Buttons ----- #####
        # Room Button Design
        self.room_lbl = Label(self.room_btn_lbl, width=300, height=4, bg='#484D4B')
        self.room_lbl.place(x=0, y=0)
        self.room_lbl.bind('<Enter>', enter)
        self.room_lbl.bind('<Leave>', leave)

        # Driver Image
        self.room_img = Image.open('images/driver-license.png').resize((40, 40))
        self.room_final_img = ImageTk.PhotoImage(self.room_img)
        self.room_img_lbl = Label(self.room_lbl, image=self.room_final_img, width=50, height=50,
                                    bg='#484D4B')
        self.room_img_lbl.place(x=5, y=0)

        # Driver Button
        self.room_btn = Button(self.room_lbl, text='Manage Room',
                                 font=('Times New Roman', 20, BOLD),
                                 bg='#484D4B', fg='#ffffff', cursor='hand2', width=14, bd=0, anchor=W,
                                 activebackground='#B316EE')
        self.room_btn.place(x=60, y=5)

        ##### ----- Logout Button Design
        self.logout_btn_lbl = Label(self.left_side_frame, width=300, height=4, bg='#484D4B')
        self.logout_btn_lbl.place(x=0, y=520)

        # Function to change properties of button while hovering the button
        def enter(event):
            self.logout_lbl.configure(bg='#B316EE')
            self.logout_img_lbl.configure(bg='#B316EE')
            self.logout_btn.config(bg='#B316EE', fg='#000000')

        def leave(event):
            self.logout_lbl.configure(bg='#484D4B')
            self.logout_img_lbl.configure(bg='#484D4B')
            self.logout_btn.config(bg='#484D4B', fg='#ffffff')

        ##### ----- Buttons ----- #####
        # Logout Button Design
        self.logout_lbl = Label(self.logout_btn_lbl, width=300, height=4, bg='#484D4B')
        self.logout_lbl.place(x=0, y=0)
        self.logout_lbl.bind('<Enter>', enter)
        self.logout_lbl.bind('<Leave>', leave)

        # Log Out Image
        self.logout_img = Image.open('images/check-out.png').resize((40, 40))
        self.logout_final_img = ImageTk.PhotoImage(self.logout_img)
        self.logout_img_lbl = Label(self.logout_lbl, image=self.logout_final_img, width=50, height=50,
                                    bg='#484D4B')
        self.logout_img_lbl.place(x=10, y=0)

        # Log Out Button
        self.logout_btn = Button(self.logout_lbl, text='Logout',
                                 font=('Times New Roman', 20, BOLD),
                                 bg='#484D4B', fg='#ffffff', cursor='hand2', width=14, bd=0, anchor=W,
                                 activebackground='#B316EE')
        self.logout_btn.place(x=60, y=5)

        ##### ----- Exit Button Design
        self.exit_btn_lbl = Label(self.left_side_frame, width=300, height=4, bg='#434D4B')
        self.exit_btn_lbl.place(x=0, y=620)

        # Function to change properties of button while hovering the button
        def enter(event):
            self.exit_lbl.configure(bg='#B316EE')
            self.exit_img_lbl.configure(bg='#B316EE')
            self.exit_btn.config(bg='#B316EE', fg='#000000')

        def leave(event):
            self.exit_lbl.configure(bg='#484D4B')
            self.exit_img_lbl.configure(bg='#484D4B')
            self.exit_btn.config(bg='#484D4B', fg='#ffffff')

        ##### ----- Buttons ----- #####
        # Driver Button Design
        self.exit_lbl = Label(self.exit_btn_lbl, width=300, height=4, bg='#484D4B')
        self.exit_lbl.place(x=0, y=0)
        self.exit_lbl.bind('<Enter>', enter)
        self.exit_lbl.bind('<Leave>', leave)

        # Log Out Image
        self.exit_img = Image.open('images/emergency-exit.png').resize((40, 40))
        self.exit_final_img = ImageTk.PhotoImage(self.exit_img)
        self.exit_img_lbl = Label(self.exit_lbl, image=self.exit_final_img, width=50, height=50,
                                  bg='#484D4B')
        self.exit_img_lbl.place(x=10, y=0)

        # Log Out Button
        self.exit_btn = Button(self.exit_lbl, text='Exit', font=('Times New Roman', 20, BOLD),
                               bg='#484D4B', fg='#ffffff', cursor='hand2', width=14, bd=0, anchor=W,
                               activebackground='#B316EE', command=self.exit_fun)
        self.exit_btn.place(x=60, y=5)

    def exit_fun(self):
        result = messagebox.askyesno('EXIT', 'Do you want to exit?')
        if result:
            self.window.destroy()

if __name__ == '__main__':
    Dashboard()