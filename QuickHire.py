from tkinter import messagebox
import pymysql
from details import *

class Entry_page:
    def __init__(self):
        try:
            self.connect_db()
            query = "select * from users"
            row_count = self.curr.execute(query)
            data = self.curr.fetchone()
            if data :
                from LoginText import LogintextClass
                LogintextClass()
            else:
                from CreateAdmin import CreateadminClass
                CreateadminClass()
        except Exception as e:
            messagebox.showerror("Unexpected Error","An unexpected error has occurred : \n"+str(e))


    def connect_db(self):
        try:
            self.conn = pymysql.connect(host=myhost, user=myuser, password=mypassword, database=mydb)
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error", "Error while connecting to the database :\n" + str(e))

if __name__ == '__main__':

    Entry_page()