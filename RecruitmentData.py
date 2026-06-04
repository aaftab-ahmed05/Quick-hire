from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import pymysql

from details import *

class RecruitmentDataClass:

    def __init__(self, wind):

        self.window = Toplevel(wind)
        self.window.title(app_name + "-Recruitments")
        ww = 1300
        wh = self.window.winfo_screenheight()

        # -------------placing window ------------------

        self.window.geometry("%dx%d+%d+%d" % (1300, wh // 1.3, 220, 75))


        # ------------------------------------colours-------------------------------
        heading_bg = "#2D3748"
        heading_fg = "#E2E8F0"
        window_bg = '#2D3748'
        lab_col_fg = '#FFFFFF'
        self.b_bg = "#222222"
        b_fg = "#F0F0F0"
        self.b_hover = "#3C5A78"
        self.window.config(bg=window_bg)

        wid_font = ("Calibri", 12, 'normal')

        # ----------------------------------widgets------------------------------------

        # --------------------------------main heading and placement of main heading--------------------------------------

        self.main_heading = Label(self.window, text='Recruitment Details', fg=heading_fg, bg=heading_bg,
                                  font=('Calibri', 25, 'bold'), borderwidth=5, relief='groove')
        self.main_heading.place(x=0, y=0, relwidth=1, height=55)

        #-----------------------------------------creating table-------------------------------------

        #	id	name	gender	dob	phone	email	address	department	jobselected	qualification	skills	applicant_image

        self.table = Treeview(self.window,columns = ['c1','c2','c3','c4','c5','c6','c7','c8','c9','c10'],height=25)
        self.table.heading('c1',text='Id')
        self.table.heading('c2',text='Name')
        self.table.heading('c3',text='Gender')
        self.table.heading('c4',text='DOB')
        self.table.heading('c5',text='Phone')
        self.table.heading('c6',text='Email')
        self.table.heading('c7',text='Address')
        self.table.heading('c8',text='Department')
        self.table.heading('c9',text='Job Selected')
        self.table.heading('c10',text='Qualification')
        self.table['show'] = 'headings'
        self.table.column('c1', width=80,anchor='center')
        self.table.column('c2', width=120,anchor='center')
        self.table.column('c3', width=120,anchor='center')
        self.table.column('c4', width=120,anchor='center')
        self.table.column('c5', width=120,anchor='center')
        self.table.column('c6', width=120,anchor='center')
        self.table.column('c7', width=150,anchor='center')
        self.table.column('c8', width=120,anchor='center')
        self.table.column('c9', width=150,anchor='center')
        self.table.column('c10',width=90,anchor='center')

        #------------------------------------------placing Table---------------------------------
        alignment = ((ww//1.3)-(ww//1.3)+140)/2
        self.table.place(x=alignment,y=100,height=350)

        # -----------------------------------------------buttons and entry widgets----------------------------------------
        wid_w = 100
        wid_h = 30
        wid_x = 30
        wid_y = 550
        diff_x = 130
        self.l1 = Label(self.window,text="Search by name : ",fg=lab_col_fg,bg=window_bg,font=wid_font,anchor="w")
        self.e1 = Entry(self.window,font=wid_font)
        self.l2 = Label(self.window,text="Search by department : ",fg=lab_col_fg,bg=window_bg,font=wid_font,anchor="w")
        self.e2 = Entry(self.window,font=wid_font)
        self.clear1 = Label(self.window,text="clear",font=wid_font,fg=lab_col_fg,bg=window_bg)
        self.clear1.bind("<Button-1>",lambda e: self.clean(self.e1,e))
        self.clear1.bind("<Enter>",lambda e: self.on_enter(self.clear1,e))
        self.clear1.bind("<Leave>",lambda e: self.on_leave(self.clear1,e))
        self.clear2 = Label(self.window,text="clear",font=wid_font,fg=lab_col_fg,bg=window_bg)
        self.clear2.bind("<Button-1>",lambda e : self.clean(self.e2,e))
        self.clear2.bind("<Enter>", lambda e: self.on_enter(self.clear2, e))
        self.clear2.bind("<Leave>", lambda e: self.on_leave(self.clear2, e))

        self.b1 = Button(self.window, text='Names', fg=b_fg, bg=self.b_bg, font=wid_font,command=self.get_data_by_name)
        self.b1.bind("<Enter>", self.b_enter)
        self.b1.bind("<Leave>", self.b_leave)
        self.b2 = Button(self.window, text='Departments', fg=b_fg, bg=self.b_bg, font=wid_font, command=self.get_data_by_department)
        self.b2.bind("<Enter>", self.b_enter)
        self.b2.bind("<Leave>", self.b_leave)
        self.b3 = Button(self.window, text='Reset Table', fg=b_fg, bg=self.b_bg, font=wid_font, command=self.Reset_tabel)
        self.b3.bind("<Enter>", self.b_enter)
        self.b3.bind("<Leave>", self.b_leave)
        self.b4 = Button(self.window, text='Print', fg=b_fg, bg=self.b_bg, font=wid_font,command=self.print_out )
        self.b4.bind("<Enter>", self.b_enter)
        self.b4.bind("<Leave>", self.b_leave)

        #-----------------------------------widget placement---------------------------------
        self.l1.place(x=alignment, y=wid_y, height=wid_h)
        alignment += diff_x
        self.e1.place(x=alignment, y=wid_y, width=wid_w, height=wid_h)
        self.clear1.place(x=alignment, y=wid_y+wid_h)
        alignment += diff_x-20
        self.b1.place(x=alignment,y=wid_y,width=wid_w,height=wid_h)
        alignment+=diff_x
        self.l2.place(x=alignment, y=wid_y, height=wid_h)
        alignment += diff_x+35
        self.e2.place(x=alignment, y=wid_y, width=wid_w, height=wid_h)
        self.clear2.place(x=alignment, y=wid_y+wid_h)
        alignment+=diff_x-20
        self.b2.place(x=alignment,y=wid_y,width=wid_w,height=wid_h)
        alignment+=diff_x+50
        self.b3.place(x=alignment,y=wid_y,width=wid_w,height=wid_h)
        alignment+=diff_x+50
        self.b4.place(x=alignment,y=wid_y,width=wid_w,height=wid_h)


        # -------------calling function that are required------------------------------
        self.connect_db()
        self.get_all_applicant_data()
        self.window.mainloop()

    # ----------------------------------------------------defining functions-------------------------------------------

    def connect_db(self):
        try:
            self.conn = pymysql.connect(host=myhost, user=myuser, password=mypassword, database=mydb)
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error", "Error while connecting to the database :\n" + str(e),
                                 parent=self.window)

    data = []

    def get_all_applicant_data(self):
        try :
            query = "select * from applicants order by id asc"
            row_count = self.curr.execute(query)
            self.data = self.curr.fetchall()
            if len(self.data)== 0 :
                messagebox.showinfo("Database Empty","No data inside database.")
            else:
                self.table.delete(*self.table.get_children())
                for row in self.data :
                    row = row[:len(row)-2]
                    self.table.insert("","end",values=row)

        except Exception as e:
            messagebox.showerror("Query Error !","Error while executing query: \n"+str(e),parent=self.window)

    def get_data_by_name(self):
        try:
            query = "select * from applicants where name = %s order by id asc"
            row_count = self.curr.execute(query,(self.e1.get()))
            self.data = self.curr.fetchall()

            if len(self.data)>=1:
                    self.table.delete(*self.table.get_children())
                    for row in self.data:
                        row = row[:len(row) - 2]
                        self.table.insert("", "end", values=row)
                    messagebox.showinfo("Success", "Data accessed successfully.", parent=self.window)
            else:
                    messagebox.showinfo("Failure", "Data not found.", parent=self.window)

        except Exception as e :
            messagebox.showerror("Query Error", "Error while executing query :\n" + str(e),
                                     parent=self.window)

    def get_data_by_department(self):
        try:
            query = "select * from applicants where department = %s order by id asc"
            row_count = self.curr.execute(query, (self.e2.get()))
            self.data = self.curr.fetchall()

            if len(self.data)>=1:
                    self.table.delete(*self.table.get_children())
                    for row in self.data:
                        row = row[:len(row) - 2]
                        self.table.insert("", "end", values=row)
                    messagebox.showinfo("Success", "Data accessed successfully.", parent=self.window)
            else:
                    messagebox.showinfo("Failure", "Data not found", parent=self.window)

        except Exception as e:
            messagebox.showerror("Query Error", "Error while executing query :\n" + str(e),
                                 parent=self.window)

    def Reset_tabel(self):
        self.table.delete(*self.table.get_children())
        self.get_all_applicant_data()

    def print_out(self):
        from PrintData import PrintClass
        import os
        pdf = PrintClass()
        headings = ["ID","Name","DOB","Phone","Email","Department","Job Selected","Qualification","Skills"]
        new_data = []
        count = 0
        for row in self.data :
            new_data.append([self.data[count][0],self.data[count][1],self.data[count][3],self.data[count][4],self.data[count][5],
                             self.data[count][7],self.data[count][8],self.data[count][9],self.data[count][10]])
            count+=1
        widths = [8, 20, 14, 16, 33, 30, 27, 16, 30]
        pdf.body(headings,new_data,widths,1)
        pdf.output("RecruitmentData.pdf")
        os.system('explorer.exe "RecruitmentData.pdf"')

#----------------------------------------------clear functions-------------------------------------------
    
    def clean(self,widget,e):
        widget.delete(0, END)

    def on_enter(self,widget, e):
        widget.config(fg="#e53935")

    def on_leave(self,widget, e):
        widget.config(fg="#FFFFFF")

    def b_enter(self, e):
        e.widget.config(bg=self.b_hover)

    def b_leave(self, e):
        e.widget.config(bg=self.b_bg)

if __name__ == '__main__':
    temp = Tk()
    RecruitmentDataClass(temp)
    temp.mainloop()
