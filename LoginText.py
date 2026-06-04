from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import Image,ImageTk

from details import *

class LogintextClass:

    def __init__(self):

        self.window = Tk()
        self.window.title(app_name + "-Login")
        self.window.attributes("-topmost",True)
        ww = self.window.winfo_screenwidth()
        wh = self.window.winfo_screenheight()

        # -------------placing window ------------------

        self.window.geometry("%dx%d+%d+%d" % (1300, wh // 1.3, (ww-600)//2, wh//4))
        self.window.maxsize(600,400)
        self.window.resizable(False, False)
        logoimg = Image.open("assets//logo.png")
        logopic = ImageTk.PhotoImage(logoimg)
        self.window.iconphoto(True, logopic)
        # ----------------------------------widgets------------------------------------

        wid_font = ("Calibri", 13, 'normal')



        #-----------------------colours-----------------------------

        heading_bg = "#2D3748"
        heading_fg = "#E2E8F0"
        window_bg = '#2D3748'
        lab_col_fg = '#FFFFFF'
        self.b_bg = "#222222"
        b_fg = "#F0F0F0"
        self.b_hover = "#3C5A78"

        self.window.config(bg=window_bg)
        # --------------------------------main heading and placement of main heading--------------------------------------

        self.main_heading = Label(self.window, text='Login', fg=heading_fg, bg=heading_bg,
                                  font=('Calibri', 25, 'bold'), borderwidth=5, relief='groove')
        self.main_heading.place(x=0, y=0, relwidth=1, height=55)

        # --------------------------------------------widgets creation---------------------------

        self.l1 = Label(self.window, text='Username', fg=lab_col_fg, bg=window_bg, font=("calibri",12,"bold"), anchor='w')
        self.l2 = Label(self.window, text='Password', fg=lab_col_fg, bg=window_bg, font=("calibri",12,"bold"), anchor='w')
        # self.another_way = Label(self.window, text='Login using face detection...',fg="grey",bg=window_bg, font=('Calibri',15,'normal'))
        # self.another_way.bind("<Button-1>",self.login_using_face)
        # self.another_way.bind("<Enter>",self.on_enter)
        # self.another_way.bind("<Leave>",self.on_leave)

        self.e1 = Entry(self.window, font=wid_font)
        self.e2 = Entry(self.window, font=wid_font,show="*")

        # ------------------------------------------------------buttons creation----------------------------------------

        self.b1 = Button(self.window, text='Login', fg=b_fg, bg=self.b_bg, font=wid_font,command=self.login_user)
        self.b1.bind("<Enter>",self.b_enter)
        self.b1.bind("<Leave>",self.b_leave)
        self.b2 = Button(self.window, text='Reset', fg=b_fg, bg=self.b_bg, font=wid_font, command=self.clear_page)
        self.b2.bind("<Enter>", self.b_enter)
        self.b2.bind("<Leave>", self.b_leave)


        # ---------------------------------------------placing widgets-------------------------------------------

        wid_w = 100
        wid_h = 30
        wid_x = 600//4
        wid_y = 80
        diff_x = 130
        diff_y = 60

        self.l1.place(x=wid_x, y=wid_y+30, width=wid_w, height=wid_h)
        self.e1.place(x=wid_x + diff_x, y=wid_y+30, width=wid_w * 2, height=wid_h)
        wid_y += diff_y
        self.l2.place(x=wid_x, y=wid_y+30, width=wid_w, height=wid_h)
        self.e2.place(x=wid_x + diff_x, y=wid_y+30, width=wid_w * 2, height=wid_h)
        wid_y += diff_y
        wid_y += diff_y

        # ----------------------------------------------placing buttons-----------------------------------------------

        self.b2.place(x=wid_x + 20, y=wid_y , width=wid_w * 1.3, height=wid_h)
        self.b1.place(x=wid_x + diff_x + 50, y=wid_y , width=wid_w * 1.3, height=wid_h)
        wid_y += diff_y
        # self.another_way.place(x=wid_x+20,y = wid_y, width=(wid_w*1.3)+diff_x+30, height=wid_h)


        # -------------calling function that are required------------------------------
        self.connect_db()

        self.window.mainloop()

    # ----------------------------------------------------defining functions-------------------------------------------

    def connect_db(self):
        try:
            self.conn = pymysql.connect(host=myhost, user=myuser, password=mypassword, database=mydb)
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error", "Error while connecting to the database :\n" + str(e),
                                 parent=self.window)

    def login_user(self):
        if self.required_info():
            try:
                query = "select * from users where username = %s and password=%s"
                row_count = self.curr.execute(query,(self.e1.get(),self.e2.get()))
                data = self.curr.fetchone()
                if data:
                    u_name = data[0]
                    u_type = data[2]
                    print(u_name,u_type)
                    # messagebox.showinfo("Success","Your are logged in .",parent = self.window)
                    from Homepage import HomeClass
                    self.window.destroy()
                    HomeClass(u_name,u_type)
                else:
                    messagebox.showerror("Wrong Login","Wrong username or password!",parent=self.window)

            except Exception as e:
                print(e)
                messagebox.showerror("Query Error","Error while executing query\n"+ str(e),parent=self.window)

    def clear_page(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)

    def required_info(self):
        if len(self.e1.get()) == 0:
            messagebox.showwarning("Empty Field", 'Enter username', parent=self.window)
            return False
        elif len(self.e2.get()) == 0 :
            messagebox.showwarning("Empty Field", 'Enter password', parent=self.window)
            return False
        return True

    # def login_using_face(self,e):
    #     from LoginFace import LoginfaceClass
    #     self.window.destroy()
    #     LoginfaceClass()

    def on_enter(self,e):
        self.another_way.config(fg="white",font=('Calibri',17,'bold'))

    def on_leave(self,e):
        self.another_way.config(fg="grey",font=('Calibri',15,'normal'))

    def b_enter(self, e):
        e.widget.config(bg=self.b_hover)

    def b_leave(self, e):
        e.widget.config(bg=self.b_bg)


if __name__ == '__main__':
    LogintextClass()
