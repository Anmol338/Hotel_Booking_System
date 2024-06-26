import mysql.connector
from tkinter import messagebox

class MyDatabase:
    __single_instance = None

    @classmethod
    def single_instance(cls):
        if not cls.__single_instance:
            cls.__single_instance = cls()

        return cls.__single_instance

    def create_conn_obj(self):
        try:
            host = "localhost"
            user = "root"
            passwd = ""
            dbase = "hotel_durbar"

            conn = mysql.connector.connect(host=host,
                                           user=user,
                                           password=passwd,
                                           database=dbase)
            return conn

        except mysql.connector.errors.DatabaseError as e:
            messagebox.showerror("Error", e)

    def create_database(self, sql, crsor):

        if sql and crsor:
            try:
                crsor.execute(sql)
            except mysql.connector.Error as e:
                if e.errno == mysql.connector.errorcode.ER_CANT_CREATE_TABLE:
                    print(str(e))
                else:
                    print(e.msg)
            else:
                print(crsor.info())
                print(crsor.column_names)

    def create_table(self, sql, crsor):

        if sql and crsor:
            try:
                crsor.execute(sql)
            except mysql.connector.Error as e:
                if e.errno == mysql.connector.errorcode.ER_CANT_CREATE_TABLE:
                    # print(str(e))
                    messagebox.showerror("Error", e)
                else:
                    # print(e.msg)
                    messagebox.showerror("Error", e.msg)
            else:
                print(crsor.column_names)

    def insert_or_update_table(self, sql, conn, crsor, value):
        if sql and crsor:
            try:
                crsor.execute(sql, value)
            except mysql.connector.Error as e:
                messagebox.showerror('Error', e.msg)
                return False
            else:
                conn.commit()
                conn.close()
                return True

    def get_data(self, sql, conn, crsor, value):

        if sql and crsor:
            try:
                crsor.execute(sql, value)
            except mysql.connector.Error as e:
                print(e.msg)
                messagebox.showerror("Error", e.msg)
            else:
                # info = crsor.fetchone()
                # info = crsor.fetchmany() / crsor.fetchall()
                info = crsor.fetchall()
                return info
            conn.close()

    def delete_data(self, sql, conn, crsor, value):
        if sql and crsor:
            try:
                crsor.execute(sql, value)
            except mysql.connector.Error as e:
                if e.errno == mysql.connector.errorcode.ER_CANT_CREATE_TABLE:
                    # print(str(e))
                    messagebox.showerror("Error", e)
                else:
                    # print(e.msg)
                    messagebox.showerror("Error", e.msg)
            else:
                conn.commit()
                print(crsor.rowcount)
                conn.close()
                return True

    def select_query(self, sql, conn, crsor):
        if sql and crsor:
            try:
                crsor.execute(sql)
            except mysql.connector.Error as e:
                print(e.msg)
                messagebox.showerror("Error", e.msg)
            else:
                info = crsor.fetchall()
                return info
            conn.close()

    def select_query_fetchone(self, sql, conn, crsor, values):
        if sql and crsor:
            try:
                crsor.execute(sql, values)
            except mysql.connector.Error as e:
                messagebox.showerror("Error", e.msg)
            else:
                info = crsor.fetchone()
                return info
            conn.close()
