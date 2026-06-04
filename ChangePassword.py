from tkinter import *
from tkinter import messagebox
import pymysql

from details import *

class ChangepasswordClass:

    def __init__(self,wind,n):
        self.name = n

        self.window = Toplevel(wind)
        self.window.title(app_name + "-Change Password")
        ww = self.window.winfo_screenwidth()
        wh = self.window.winfo_screenheight()

        # -------------placing window ------------------

        self.window.geometry("%dx%d+%d+%d" % (1300, wh // 1.3, (ww-600)//2, wh//4))
        self.window.maxsize(600,400)
        self.window.resizable(False, False)
        # -----------------------colours-----------------------------

        heading_bg = "#2D3748"
        heading_fg = "#E2E8F0"
        window_bg = '#2D3748'
        lab_col_fg = '#FFFFFF'
        self.b_bg = "#222222"
        b_fg = "#F0F0F0"
        self.b_hover = "#3C5A78"

        self.window.config(bg=window_bg)

        wid_font = ("Calibri", 13, 'normal')

        # ----------------------------------widgets------------------------------------


        # --------------------------------main heading and placement of main heading--------------------------------------

        self.main_heading = Label(self.window, text='Change Password', fg=heading_fg, bg=heading_bg,
                                  font=('Calibri', 25, 'bold'), borderwidth=5, relief='groove')
        self.main_heading.place(x=0, y=0, relwidth=1, height=55)

        # --------------------------------------------widgets creation---------------------------

        self.l1 = Label(self.window, text='Current Password', fg=lab_col_fg, bg=window_bg, font=wid_font, anchor='w')
        self.l2 = Label(self.window, text='New Password', fg=lab_col_fg, bg=window_bg, font=wid_font, anchor='w')
        self.l3 = Label(self.window, text='Confirm Password', fg=lab_col_fg, bg=window_bg, font=wid_font, anchor='w')

        self.e1 = Entry(self.window, font=wid_font)
        self.e2 = Entry(self.window, font=wid_font,show="*")
        self.e3 = Entry(self.window, font=wid_font,show="*")

        # ------------------------------------------------------buttons creation----------------------------------------

        self.b1 = Button(self.window, text='Change', fg=b_fg, bg=self.b_bg, font=wid_font,command=self.new_password)
        self.b1.bind("<Enter>", self.b_enter)
        self.b1.bind("<Leave>", self.b_leave)
        self.b2 = Button(self.window, text='Reset' , fg=b_fg, bg=self.b_bg, font=wid_font, command=self.clear_page)
        self.b2.bind("<Enter>", self.b_enter)
        self.b2.bind("<Leave>", self.b_leave)

        # ---------------------------------------------placing widgets-------------------------------------------

        wid_w = 130
        wid_h = 30
        wid_x = 500//4
        wid_y = 80
        diff_x = 150
        diff_y = 60

        self.l1.place(x=wid_x, y=wid_y+30, width=wid_w, height=wid_h)
        self.e1.place(x=wid_x + diff_x, y=wid_y+30, width=wid_w * 1.5, height=wid_h)
        wid_y += diff_y
        self.l2.place(x=wid_x, y=wid_y+30, width=wid_w, height=wid_h)
        self.e2.place(x=wid_x + diff_x, y=wid_y+30, width=wid_w * 1.5, height=wid_h)
        wid_y += diff_y
        self.l3.place(x=wid_x, y=wid_y+30, width=wid_w, height=wid_h)
        self.e3.place(x=wid_x + diff_x, y=wid_y+30, width=wid_w * 1.5, height=wid_h)
        wid_y += diff_y
        wid_y += diff_y

        # ----------------------------------------------placing buttons-----------------------------------------------

        self.b2.place(x=wid_x + 20, y=wid_y , width=wid_w , height=wid_h)
        self.b1.place(x=wid_x + diff_x + 50, y=wid_y , width=wid_w , height=wid_h)
        wid_y += diff_y


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

    def new_password(self):
        if self.required_info():
            if self.e2.get() == self.e3.get():
                try:
                    query = "update users set password=%s where username=%s and password=%s"
                    row_count = self.curr.execute(query,(self.e2.get(),self.name,self.e1.get()))
                    if row_count == 1:
                        self.conn.commit()
                        messagebox.showinfo("Success","Password changed successfully.",parent=self.window)
                    else :
                        messagebox.showinfo("Failure","Password not changed",parent=self.window)

                except Exception as e:
                    messagebox.showerror("Query Error","Error while executing query\n"+ str(e),parent=self.window)

            else:
                messagebox.showerror("Mismatch Error ","Confirmed password is not same.",parent=self.window)

    def clear_page(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)

    def required_info(self):
        if len(self.e1.get()) == 0:
            messagebox.showwarning("Empty Field", 'Enter current password', parent=self.window)
            return False
        elif len(self.e2.get()) == 0 :
            messagebox.showwarning("Empty Field", 'Enter new password', parent=self.window)
            return False
        elif len(self.e3.get()) == 0 :
            messagebox.showwarning("Empty Field", 'Confirm password', parent=self.window)
            return False
        return True

    def b_enter(self, e):
        e.widget.config(bg=self.b_hover)

    def b_leave(self, e):
        e.widget.config(bg=self.b_bg)



