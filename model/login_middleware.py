from database import conn as connection
from tkinter import messagebox

##### ----- LogIn_Middleware Class ----- #####
class LogIn_Middleware:
    ##### ----- Defining Initial attributes of the class LogIn_Middleware ----- #####
    def __init__(self):
        self._user_id = ""
        self._username = ""
        self._password = ""
        self._usertype = ""
        self._userstatus = ""
        self._fullname = ""

    ##### ----- Function to return the initial variable data ----- #####
    @property
    def get_user_id(self):
        return self._user_id

    @property
    def get_username(self):
        return self._username

    @property
    def get_password(self):
        return self._password

    @property
    def get_usertype(self):
        return self._usertype

    @property
    def get_userstatus(self):
        return self._userstatus

    @property
    def get_fullname(self):
        return self._fullname

    ##### ----- Function to return the initial variable data ----- #####

    ##### ----- Function to set the initial variable data ----- #####
    @get_user_id.setter
    def set_user_id(self, new_user_id):
        self._user_id = new_user_id

    @get_username.setter
    def set_username(self, username):
        self._username = username

    @get_password.setter
    def set_password(self, password):
        self._password = password

    @get_usertype.setter
    def set_usertype(self, usertype):
        self._usertype = usertype

    @get_userstatus.setter
    def set_userstatus(self, userstatus):
        self._userstatus = userstatus

    @get_fullname.setter
    def set_full_name(self, fullname):
        self._fullname = fullname

    ##### ----- Function to set the initial variable data ----- #####
    def __str__(self):
        return self.get_username + self.get_usertype + self.get_userstatus

    def database_data(self):
        db = connection.MyDatabase()
        conn = db.create_conn_obj()
        if conn:
            mycursor = conn.cursor()
            sql = "SELECT user_id, username, user_type, user_status, full_name from user where username= %s and password= %s"
            values = (self.get_username, self.get_password)
            data = db.get_data(sql, conn, mycursor, values)
            if len(data) > 0:
                self.set_user_id = data[0][0]
                self.set_username = data[0][1]
                self.set_usertype = data[0][2]
                self.set_userstatus = data[0][3]
                self.set_full_name = data[0][4]

            else:
                messagebox.showerror("Error", "Username and password did not match !!")

if __name__ == '__main__':
    test = LogIn_Middleware()
    test.set_username = 'admin@gmail.com'
    test.set_password = 'admin123'
    test.database_data()
    print(str(test.get_user_id) + ' ' + test.get_username + ' ' + test.get_usertype + ' ' + test.get_userstatus + ' ' + test.get_fullname)
