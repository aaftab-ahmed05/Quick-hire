from tkinter import *
from tkinter import messagebox
import pymysql
from tkcalendar import DateEntry

from details import *


class AddjobsClass:

    def __init__(self, wind):

        self.window = Toplevel(wind)
        self.window.title(app_name + "-Add jobs")
        ww = 1300
        wh = self.window.winfo_screenheight()

        # -------------placing window ------------------

        self.window.geometry("%dx%d+%d+%d" % (1300, wh // 1.3, ww//4, 75))
        self.window.maxsize(int(ww//2)+int(ww*30/100), int(wh // 1.3))
        self.window.resizable(False, False)

        #------------------------------colours---------------------------------
        heading_bg = "#2D3748"
        heading_fg = "#E2E8F0"
        window_bg = '#2D3748'
        lab_col_fg = '#FFFFFF'
        self.b_bg = "#222222"
        b_fg = "#F0F0F0"
        self.b_hover = "#3C5A78"
        self.window.config(bg=window_bg)

        wid_font = ("Calibri", 13, 'normal')

        # ------------------------------------frame creation and placing------------------------------------


        frame_width = ww * 30 / 100
        frame_height = wh - 55
        self.f1 = Frame(self.window)
        self.f1.place(x=ww//2, y=55, width=ww * 30 / 100, height=wh - 55)

        self.f_heading = Label(self.f1, text="Manage Data", font=('Calibri', 18, 'normal'))
        self.f_heading.place(x=0, y=10, relwidth=1, height=30)

        # ----------------------------------widgets------------------------------------

        # --------------------------------main heading and placement of main heading--------------------------------------

        self.main_heading = Label(self.window, text='''Add jobs''', fg=heading_fg, bg=heading_bg,
                                  font=('Calibri', 25, 'bold'), borderwidth=5, relief='groove')
        self.main_heading.place(x=0, y=0, relwidth=1, height=55)

        # --------------------------------------------widgets creation---------------------------

        self.l1 = Label(self.window, text='Department', fg=lab_col_fg, bg=window_bg, font=wid_font, anchor='w')
        self.l2 = Label(self.window, text='Job Id', fg=lab_col_fg, bg=window_bg, font=wid_font, anchor='w')
        self.l3 = Label(self.window, text='Job Title', fg=lab_col_fg, bg=window_bg, font=wid_font, anchor='w')
        self.l4 = Label(self.window, text='Vacancies', fg=lab_col_fg, bg=window_bg, font=wid_font, anchor='w')
        self.l5 = Label(self.window, text='Last Date', fg=lab_col_fg, bg=window_bg, font=wid_font, anchor='w')

        self.e1 = Entry(self.window, font=wid_font)
        self.e2 = Entry(self.window, font=wid_font)
        self.e3 = Entry(self.window, font=wid_font)
        self.e4 = Entry(self.window, font=wid_font)
        self.e5 = DateEntry(self.window, borderwidth=2, year=2025, date_pattern='y-mm-dd', font=wid_font,state = 'normal')
        self.e5.delete(0,END)



        # ------------------------------------------------------buttons----------------------------------------

        self.b1 = Button(self.window, text='Save',   fg=b_fg, bg=self.b_bg, font=wid_font, command=self.save_data_db)
        self.b1.bind("<Enter>", self.b_enter)
        self.b1.bind("<Leave>", self.b_leave)
        self.b2 = Button(self.window, text='Reset',  fg=b_fg, bg=self.b_bg, font=wid_font, command=self.clear_page)
        self.b2.bind("<Enter>", self.b_enter)
        self.b2.bind("<Leave>", self.b_leave)
        self.b3 = Button(self.f1, text='Fetch Data', fg=b_fg, bg=self.b_bg, font=wid_font,command=self.fetch_data_db)
        self.b3.bind("<Enter>", self.b_enter)
        self.b3.bind("<Leave>", self.b_leave)
        self.b4 = Button(self.f1, text='Update Data',fg=b_fg, bg=self.b_bg, font=wid_font,command=self.update_data_db)
        self.b4.bind("<Enter>", self.b_enter)
        self.b4.bind("<Leave>", self.b_leave)
        self.b5 = Button(self.f1, text='Delete Data',fg=b_fg, bg=self.b_bg, font=wid_font,command=self.delete_data_db)
        self.b5.bind("<Enter>", self.b_enter)
        self.b5.bind("<Leave>", self.b_leave)

        # ---------------------------------------------placing widgets-------------------------------------------

        wid_w = 100
        wid_h = 30
        wid_x = 30
        wid_y = 100
        diff_x = 130
        diff_y = 60


        self.l1.place(x=wid_x+100, y=wid_y, width=wid_w, height=wid_h)
        self.e1.place(x=wid_x + diff_x+100, y=wid_y, width=wid_w * 2, height=wid_h)
        wid_y += diff_y+20
        self.l2.place(x=wid_x+100, y=wid_y, width=wid_w, height=wid_h)
        self.e2.place(x=wid_x + diff_x+100, y=wid_y, width=wid_w * 2, height=wid_h)
        wid_y += diff_y+20
        self.l3.place(x=wid_x+100, y=wid_y, width=wid_w, height=wid_h)
        self.e3.place(x=wid_x + diff_x+100, y=wid_y, width=wid_w *2, height=wid_h)
        wid_y += diff_y+20
        self.l4.place(x=wid_x+100, y=wid_y, width=wid_w, height=wid_h)
        self.e4.place(x=wid_x + diff_x+100, y=wid_y, width=wid_w * 2, height=wid_h)
        wid_y += diff_y+20
        self.l5.place(x=wid_x+100, y=wid_y, width=wid_w, height=wid_h)
        self.e5.place(x=wid_x + diff_x+100, y=wid_y, width=wid_w * 2, height=wid_h)
        wid_y += diff_y+20


        # ----------------------------------------------placing buttons outside the frame -----------------------------------------------

        self.b1.place(x=wid_x+100, y=wid_y, width=wid_w * 1.3, height=wid_h)
        self.b2.place(x=wid_x + diff_x + 130, y=wid_y, width=wid_w * 1.3, height=wid_h)



        # --------------------------------------creating widgets for frame and adding buttons--------------------------

        # ---------------widgets creation and placing-----------------------------
        self.info_label = Label(self.f1, text="Enter job ID below to manage the data", fg='gray',
                                font=wid_font)
        self.info_label.place(x=0, y=50, relwidth=1)
        self.framelabel = Label(self.f1, text="Job ID:", font=('Calibri', 12, 'bold'))
        self.fetch_widget = Entry(self.f1, font=wid_font)
        self.framelabel.place(x=frame_width / 4, y=150, width=wid_w + 20, height=wid_h)
        self.fetch_widget.place(x=frame_width / 4 + diff_x, y=150, width=wid_w, height=wid_h)
        self.clear_label = Label(self.f1, text='clear', font=('Calibri', 11, 'normal'))
        self.clear_label.bind("<Button-1->", self.clean)
        self.clear_label.bind("<Enter>", self.on_enter)
        self.clear_label.bind("<Leave>", self.on_leave)
        self.clear_label.place(x=frame_width / 4 + diff_x, y=190)

        # ------------------placing buttons inside the frame----------------------
        btn_y = 160
        btn_y += diff_y + 50

        self.b3.place(x=(frame_width - wid_w * 1.3) / 2, y=btn_y, width=wid_w * 1.3, height=wid_h)
        btn_y += diff_y + 30
        self.b4.place(x=(frame_width - wid_w * 1.3) / 2, y=btn_y, width=wid_w * 1.3, height=wid_h)
        btn_y += diff_y + 30
        self.b5.place(x=(frame_width - wid_w * 1.3) / 2, y=btn_y, width=wid_w * 1.3, height=wid_h)
        btn_y += diff_y + 30
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


    def save_data_db(self):

        try:
            # ----------------------------------id name gender dob phone email address jobtype jobname qualification skills interviewdate----------------------------------
            if self.required_info():

                query = "insert into addjobs values(%s,%s,%s,%s,%s)"
                row_count = self.curr.execute(query,
                                              (self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get(),self.e5.get_date()))
                self.conn.commit()

                if row_count == 1:
                    messagebox.showinfo("Success", "Data saved successfully", parent=self.window)
                else:
                    messagebox.showinfo("Failure", "Data not saved ", parent=self.window)
                self.clear_page()

        except Exception as e:
            messagebox.showwarning("Query Error", "Error while executing query :\n" + str(e), parent=self.window)


    def fetch_data_db(self):
        try:
            query = "select * from addjobs  where job_id=%s"
            row_count = self.curr.execute(query, self.fetch_widget.get())
            data = self.curr.fetchone()
            self.clear_page()
            self.e1.insert(0, data[0])
            self.e2.insert(0, data[1])
            self.e3.insert(0,data[2])
            self.e4.insert(0,data[3])
            self.e5.insert(0, data[4])


            if row_count == 1:
                messagebox.showinfo("Success", "Data Fetched successfully", parent=self.window)
            else:
                messagebox.showinfo("Failure", "Data not Fetched ", parent=self.window)

        except Exception as e:
            messagebox.showwarning("Query Error", "Error while executing query :\n" + str(e), parent=self.window)


    def update_data_db(self):
        # -department job_id job_title vacandies last_date

        try:
            if self.required_info():
                query = "update addjobs set department=%s,job_title=%s,vacancies=%s,last_date=%s where job_id = %s"
                row_count = self.curr.execute(query,
                                              (self.e1.get(), self.e3.get(), self.e4.get(), self.e5.get_date(), self.e2.get()))
                self.conn.commit()

                if row_count == 1:
                    messagebox.showinfo("Success", "Data updated successfully", parent=self.window)
                    self.clear_page()

                else:
                    messagebox.showinfo("Failure", "Data not updated ", parent=self.window)

        except Exception as e:
            messagebox.showwarning("Query Error", "Error while executing query :\n" + str(e), parent=self.window)


    def delete_data_db(self):

        try:
            query = "delete from addjobs where job_id=%s"
            row_count = self.curr.execute(query, self.fetch_widget.get())

            ans = messagebox.askquestion("Confirmation", "Do you really want to delete the data ?", parent=self.window)
            if ans == 'yes':
                self.conn.commit()
                if row_count == 1:
                    messagebox.showinfo("Success", 'Data deleted Successfully', parent=self.window)
                else:
                    messagebox.showwarning("Failure", 'Data not deleted', parent=self.window)


        except Exception as e:
            messagebox.showerror("Query Error", "Error while executing query :\n" + str(e), parent=self.window)


    def clear_page(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0,END)
        self.e4.delete(0, END)
        self.e5.delete(0, END)


    def required_info(self):
        if len(self.e1.get()) < 2 :
            messagebox.showwarning("Empty Field", 'Please enter a valid department', parent=self.window)
            return False
        elif len(self.e2.get()) !=4 or not self.e2.get().isdigit():
            messagebox.showwarning("Empty Field", 'Job id must contain 4 characters', parent=self.window)
            return False
        elif len(self.e3.get()) < 5:
            messagebox.showwarning("Empty Field", 'Please enter a valid job title', parent=self.window)
            return False
        elif len(self.e4.get()) == 0 or self.e4.get().strip() == '':
            messagebox.showwarning("Empty Field", 'Vacancy must be a number', parent=self.window)
            return False
        elif len(self.e5.get()) < 1:
            messagebox.showwarning("Empty Field", 'Please select a valid date', parent=self.window)
            return False

        return True

    # -------------------------------clean function for frame ----------------------------
    def clean(self, e):
        self.fetch_widget.delete(0, END)

    def on_enter(self, e):
        self.clear_label.config(fg="#e53935")

    def on_leave(self, e):
        self.clear_label.config(fg="black")

    def b_enter(self, e):
        e.widget.config(bg=self.b_hover)

    def b_leave(self, e):
        e.widget.config(bg=self.b_bg)


if __name__ == '__main__':
    temp = Tk()
    AddjobsClass(temp)
    temp.mainloop()
