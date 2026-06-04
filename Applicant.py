from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox
import pymysql
from tkcalendar import DateEntry
from PIL import Image,ImageTk
from details import *


class ApplicantClass:

    def __init__(self,wind):

        self.window = Toplevel(wind)
        self.window.title(app_name+"-Applicant")
        ww = 1300
        wh = self.window.winfo_screenheight()

        # -------------placing window ------------------

        self.window.geometry("%dx%d+%d+%d" %(1300,wh//1.3,220,75))
        self.window.resizable(False,False)

        #------------------------------------colours-------------------------------
        heading_bg = "#2D3748"
        heading_fg = "#E2E8F0"
        window_bg =  '#2D3748'
        lab_col_fg = '#FFFFFF'
        self.b_bg = "#222222"
        b_fg = "#F0F0F0"
        self.b_hover = "#3C5A78"
        self.window.config(bg=window_bg)

        wid_font=("Calibri",13,'normal')

        #------------------------------------frame creation and placing------------------------------------

        frame_width = ww*30/100
        frame_height = wh-55
        self.f1 = Frame(self.window)
        self.f1.place(x=ww*70/100,y=55,width=ww*30/100,height=wh-55)

        self.f_heading = Label(self.f1,text="Manage Data",font=('Calibri',18,'normal'))
        self.f_heading.place(x=0,y=10,relwidth=1,height=30)

        # ----------------------------------widgets------------------------------------



        #--------------------------------main heading and placement of main heading--------------------------------------

        self.main_heading = Label(self.window,text='''Applicant's Profile''',fg=heading_fg,bg=heading_bg,font=('Calibri',25,'bold'),borderwidth=5,relief='groove')
        self.main_heading.place(x=0, y=0, relwidth=1,height=55 )

        #--------------------------------------------widgets creation---------------------------

        self.imglabel = Label(self.window,borderwidth=2.5,relief='sunken')
        self.label_for_image = Label(self.window, text= 'Add image',fg=lab_col_fg,bg=window_bg,font=wid_font,anchor='w')
        self.imglabel.bind('<Button-1>',self.set_profile_img)
        self.l1 = Label(self.window, text= 'Id',           fg=lab_col_fg,bg=window_bg,font=wid_font,anchor='w')
        self.l2 = Label(self.window, text= 'Name',         fg=lab_col_fg,bg=window_bg,font=wid_font,anchor='w')
        self.l3 = Label(self.window, text='Gender',        fg=lab_col_fg,bg=window_bg,font=wid_font,anchor='w')
        self.l4 = Label(self.window, text= 'DOB',          fg=lab_col_fg,bg=window_bg,font=wid_font,anchor='w')
        self.l5 = Label(self.window, text= 'Phone',        fg=lab_col_fg,bg=window_bg,font=wid_font,anchor='w')
        self.l6 = Label(self.window, text= 'Email',        fg=lab_col_fg,bg=window_bg,font=wid_font,anchor='w')
        self.l7 = Label(self.window, text= 'Address',      fg=lab_col_fg,bg=window_bg,font=wid_font,anchor='w')
        self.l8 = Label(self.window, text= 'Department',     fg=lab_col_fg,bg=window_bg,font=wid_font,anchor='w')
        self.l9 = Label(self.window, text= 'Select job',   fg=lab_col_fg,bg=window_bg,font=wid_font,anchor='w')
        self.l10 = Label(self.window,text= 'Qualification',fg=lab_col_fg,bg=window_bg,font=wid_font,anchor='w')
        self.l11 = Label(self.window,text= 'Skills',       fg=lab_col_fg,bg=window_bg,font=wid_font,anchor='w')


        self.e1 = Entry(self.window,font=wid_font)
        self.e2 = Entry(self.window,font=wid_font)
        self.gender = StringVar(value=0)
        self.r1 = Radiobutton(self.window,text="Male",  value="Male",  variable=self.gender,font=("Calibri",13,"bold"),bg=window_bg,fg="#e86231")
        self.r2 = Radiobutton(self.window,text="Female",value="Female",variable=self.gender,font=("Calibri",13,"bold"),bg=window_bg,fg="#e86231")
        self.e4 = DateEntry(self.window,borderwidth=2,year=2000,date_pattern='y-mm-dd',font=wid_font)
        self.e4.delete(0,END)
        self.e5 = Entry(self.window,font=wid_font)
        self.e6 = Entry(self.window,font=wid_font)
        self.t1 = Text(self.window, font=wid_font)
        self.var1 = StringVar()
        self.c1 = Combobox(self.window,textvariable=self.var1,state='readonly',font=wid_font)
        self.c1.bind("<Button-1>",lambda e : self.get_department(e))
        self.c1.set(value='--select department--')
        self.var2=StringVar()
        self.c2 = Combobox(self.window,textvariable=self.var2,state='readonly',font=wid_font)
        self.c2.bind("<Button-1>",lambda e : self.get_jobs(e))
        self.c2.set(value='--select job--')
        self.e10 = Entry(self.window,font=wid_font)
        self.t2 = Text(self.window,font=wid_font)



        #------------------------------------------------------buttons----------------------------------------

        self.b1 = Button(self.window,text= 'Save',   fg=b_fg, bg=self.b_bg, font=wid_font, command=self.save_data_db)
        self.b1.bind("<Enter>", self.b_enter)
        self.b1.bind("<Leave>", self.b_leave)
        self.b2 = Button(self.window, text='Reset',  fg=b_fg, bg=self.b_bg, font=wid_font, command=self.clear_page)
        self.b2.bind("<Enter>", self.b_enter)
        self.b2.bind("<Leave>", self.b_leave)
        self.b3 = Button(self.f1, text='Fetch Data', fg=b_fg, bg=self.b_bg, font=wid_font, command=self.fetch_data_db)
        self.b3.bind("<Enter>", self.b_enter)
        self.b3.bind("<Leave>", self.b_leave)
        self.b4 = Button(self.f1, text='Update Data',fg=b_fg, bg=self.b_bg, font=wid_font, command=self.update_data_db)
        self.b4.bind("<Enter>", self.b_enter)
        self.b4.bind("<Leave>", self.b_leave)
        self.b5 = Button(self.f1, text='Delete Data',fg=b_fg, bg=self.b_bg, font=wid_font, command=self.delete_data_db)
        self.b5.bind("<Enter>", self.b_enter)
        self.b5.bind("<Leave>", self.b_leave)

        #---------------------------------------------placing widgets-------------------------------------------

        wid_w = 100
        wid_h = 30
        wid_x = 30
        wid_y = 80
        diff_x = 130
        diff_y = 60

        #-------------------------------------block 1-------------------------------
        self.imgsize = 175
        self.defaultimg = 'default.png'
        self.actual_name = 'default.png'
        self.default = ImageTk.PhotoImage(Image.open("applicants_images//"+self.defaultimg).resize((self.imgsize, self.imgsize)))
        self.label_for_image.place(x=wid_x,y=wid_y+70,width=wid_w,height=wid_h)
        self.imglabel.config(image=self.default)
        self.imglabel.place(x=wid_x + diff_x, y=wid_y, width=self.imgsize, height=self.imgsize)
        wid_y += diff_y*3.5
        self.l1.place(x=wid_x,y=wid_y,width=wid_w,height=wid_h)
        self.e1.place(x=wid_x+diff_x,y=wid_y,width=wid_w*2,height=wid_h)
        wid_y+=diff_y
        self.l2.place(x=wid_x, y=wid_y, width=wid_w, height=wid_h)
        self.e2.place(x=wid_x + diff_x, y=wid_y, width=wid_w * 2, height=wid_h)
        wid_y += diff_y
        self.l3.place(x=wid_x, y=wid_y, width=wid_w, height=wid_h)
        self.r1.place(x=wid_x + diff_x, y=wid_y, width=wid_w-20, height=wid_h)
        self.r2.place(x=wid_x+diff_x+120, y=wid_y, width=wid_w-20, height=wid_h)
        wid_y += diff_y
        self.l4.place(x=wid_x, y=wid_y, width=wid_w, height=wid_h)
        self.e4.place(x=wid_x + diff_x, y=wid_y, width=wid_w * 2, height=wid_h)
        wid_y += diff_y
        self.l5.place(x=wid_x , y=wid_y, width=wid_w, height=wid_h)
        self.e5.place(x=wid_x  + diff_x, y=wid_y, width=wid_w * 2, height=wid_h)
        wid_y += diff_y


        # -------------------------------------block 2-------------------------------

        wid_y = 80

        self.l6.place(x=wid_x*14, y=wid_y, width=wid_w, height=wid_h)
        self.e6.place(x=wid_x*14 + diff_x, y=wid_y, width=wid_w * 2, height=wid_h)
        wid_y += diff_y
        self.l7.place(x=wid_x*14, y=wid_y, width=wid_w, height=wid_h)
        self.t1.place(x=wid_x*14 + diff_x, y=wid_y, width=wid_w * 2, height=wid_h * 2)
        wid_y += diff_y
        wid_y += diff_y/2
        self.l8.place(x=wid_x*14,y=wid_y,width=wid_w,height=wid_h)
        self.c1.place(x=wid_x*14+diff_x,y=wid_y,width=wid_w*2,height=wid_h)
        wid_y += diff_y
        self.l9.place(x=wid_x*14,y=wid_y,width=wid_w,height=wid_h)
        self.c2.place(x=wid_x*14+diff_x,y=wid_y,width=wid_w*2,height=wid_h)
        wid_y += diff_y
        self.l10.place(x=wid_x*14,y=wid_y,width=wid_w,height=wid_h)
        self.e10.place(x=wid_x*14+diff_x,y=wid_y,width=wid_w*2,height=wid_h)
        wid_y += diff_y
        self.l11.place(x=wid_x*14,y=wid_y,width=wid_w,height=wid_h)
        self.t2.place(x=wid_x*14+diff_x,y=wid_y,width=wid_w*2,height=wid_h*2)
        wid_y += diff_y*2.7


        #----------------------------------------------placing buttons outside the frame -----------------------------------------------

        self.b1.place(x=wid_x*17,y=wid_y-40,width=wid_w*1.3,height=wid_h)
        self.b2.place(x=wid_x*17+diff_x+30,y=wid_y-40,width=wid_w*1.3,height=wid_h)

        #--------------------------------------creating widgets for frame and adding buttons--------------------------

        #---------------widgets creation and placing-----------------------------
        self.info_label = Label(self.f1, text="Enter applicant's ID below to manage their data",fg='gray',font=wid_font)
        self.info_label.place(x=0,y=50,relwidth=1)
        self.framelabel = Label(self.f1,text="Applicant's ID:",font=('Calibri',12,'bold'))
        self.fetch_widget = Entry(self.f1,font=wid_font)
        self.framelabel.place(x=frame_width/4,y=150,width=wid_w+20,height=wid_h)
        self.fetch_widget.place(x=frame_width/4 + diff_x,y=150,width=wid_w,height=wid_h)
        self.clear_label = Label(self.f1,text='clear',font=('Calibri',11,'normal'))
        self.clear_label.bind("<Button-1>",self.clean)
        self.clear_label.bind("<Enter>",self.on_enter)
        self.clear_label.bind("<Leave>",self.on_leave)
        self.clear_label.place(x=frame_width/4 + diff_x,y=190)

        #------------------placing buttons inside the frame----------------------
        btn_y = 160
        btn_y+=diff_y+50

        self.b3.place(x=(frame_width-wid_w*1.3)/2 ,y=btn_y , width=wid_w*1.3, height=wid_h)
        btn_y+=diff_y+30
        self.b4.place(x=(frame_width - wid_w * 1.3) / 2, y=btn_y, width=wid_w * 1.3, height=wid_h)
        btn_y += diff_y+30
        self.b5.place(x=(frame_width - wid_w * 1.3) / 2, y=btn_y, width=wid_w * 1.3, height=wid_h)
        btn_y += diff_y+30

        #-------------calling function that are required------------------------------
        self.connect_db()


        self.window.mainloop()

    #----------------------------------------------------defining functions-------------------------------------------

    def connect_db(self):
        try:
            self.conn = pymysql.connect(host=myhost,user=myuser,password=mypassword,database=mydb)
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error","Error while connecting to the database :\n"+str(e),parent=self.window)


    def set_profile_img(self, e):
        filename = askopenfilename(
            filetypes=[('Pictures', '*.jpg;*.png;*.jpeg'), ('PNG Images', '*.png'), ('JPG Images', "*.jpg")],
            parent=self.window)
        if filename != '':
                self.profileimg = Image.open(filename).resize((self.imgsize, self.imgsize))
                self.profilepic = ImageTk.PhotoImage(self.profileimg)
                self.imglabel.config(image=self.profilepic)
                filename = filename.split('/')[-1]
                import time
                add_time = time.time()
                self.actual_name = (str(int(add_time)))[5:] + filename
        else:
            messagebox.showwarning("Image Missing","Profile image not selected.",parent=self.window)


    def save_data_db(self):

        try:
            #----------------------------------id name gender dob phone email address jobtype jobname qualification skills interviewdate----------------------------------
            if self.required_info():

                query = "insert into applicants values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                row_count = self.curr.execute(query,(self.e1.get(),self.e2.get(),self.gender.get(),
                            self.e4.get_date(),self.e5.get(),self.e6.get(),self.t1.get('0.0',END),self.var1.get()
                            ,self.var2.get(),self.e10.get(),self.t2.get('0.0',END),self.actual_name))
                self.conn.commit()

                if row_count == 1:
                    if self.actual_name!=self.defaultimg :
                        self.profileimg.save("applicants_images//"+self.actual_name)
                    messagebox.showinfo("Success","Data saved successfully",parent = self.window)
                    self.clear_page()
                else:
                    messagebox.showinfo("Failure","Data not saved ",parent = self.window)

        except Exception as e:
            messagebox.showwarning("Query Error","Error while executing query :\n"+str(e),parent=self.window)

    
    def fetch_data_db(self):
        try:
            query = "select * from applicants  where id=%s"
            row_count = self.curr.execute(query,self.fetch_widget.get())
            data = self.curr.fetchone()
            self.clear_page()
            self.e1.insert(0,data[0])
            self.e2.insert(0,data[1])
            self.gender.set(data[2])
            self.e4.set_date(data[3])
            self.e5.insert(0,data[4])
            self.e6.insert(0,data[5])
            self.t1.insert(0.0,data[6])
            self.var1.set(data[7])
            self.var2.set(data[8])
            self.e10.insert(0,data[9])
            self.t2.insert(0.0,data[10])
            self.oldname = data[11]
            self.actual_name = data[11]
            self.profileimg = Image.open("applicants_images//"+self.actual_name).resize((self.imgsize,self.imgsize))
            self.profilepic = ImageTk.PhotoImage(self.profileimg)
            self.imglabel.config(image=self.profilepic)

            if row_count == 1:
                # messagebox.showinfo("Success", "Data Fetched successfully", parent=self.window)
                print('fetched')
            else:
                messagebox.showinfo("Failure", "Data not Fetched ", parent=self.window)

        except Exception as e:
            messagebox.showwarning("Query Error", "No matching id :\n" + str(e), parent=self.window)


    def update_data_db(self):
        # ----------------------id name gender dob phone email address jobselected qualification skills interviewdate----------------------------

        try:
            if self.required_info():
                query = "update applicants set name=%s,gender=%s,dob=%s,phone=%s,email=%s,address=%s,department=%s,jobselected=%s,qualification=%s,skills=%s,applicant_image=%s  where id = %s"
                row_count = self.curr.execute(query, (self.e2.get(),self.gender.get(),self.e4.get_date(),self.e5.get(),
                                                      self.e6.get(),self.t1.get('1.0',END).strip(),
                                                      self.var1.get(),self.var2.get(),self.e10.get(),self.t2.get('1.0',END).strip(),self.actual_name,self.e1.get()))
                self.conn.commit()

                if row_count == 1:
                    messagebox.showinfo("Success", "Data updated successfully", parent=self.window)
                    if self.actual_name!=self.oldname:
                        self.profileimg.save('applicants_images//'+self.actual_name)
                        if self.oldname!= self.defaultimg:
                            import os
                            os.remove("applicants_images//"+self.oldname)

                    self.clear_page()

                else:
                    messagebox.showinfo("Failure", "Data not updated ", parent=self.window)

        except Exception as e:
            messagebox.showwarning("Query Error", "Error while executing query :\n" + str(e), parent=self.window)


    def delete_data_db(self):

        try :
            query = "delete from applicants where id=%s"
            row_count = self.curr.execute(query,self.fetch_widget.get())

            ans = messagebox.askquestion("Confirmation","Do you really want to delete the data ?",parent = self.window)
            if ans == 'yes':
                self.conn.commit()
                self.clear_page()
                if row_count == 1 :
                    if self.actual_name!=self.defaultimg:
                        import os
                        os.remove('applicants_images//'+self.actual_name)

                    messagebox.showinfo("Success",'Data deleted Successfully',parent=self.window)
                else :
                    messagebox.showwarning("Failure",'Data not deleted',parent=self.window)


        except Exception as e:
            messagebox.showerror("Query Error","Error while executing query :\n"+str(e),parent=self.window)


    def clear_page(self):
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.gender.set(None)
        self.e4.delete(0,END)
        self.e5.delete(0,END)
        self.e6.delete(0,END)
        self.t1.delete(0.0,END)
        self.c1.set(value='--select department--')
        self.c2.set(value='--select job--')
        self.e10.delete(0,END)
        self.t2.delete(0.0,END)
        self.imglabel.config(image=self.default)
        # self.actual_name='default.png'


    def required_info(self):
        if len(self.e1.get())<4 or not self.e1.get().isdigit():
            messagebox.showwarning("Empty Field",'Please enter a valid Id',parent=self.window)
            return False
        elif len(self.e2.get())<2 :
            messagebox.showwarning("Empty Field",'Please enter a valid name',parent=self.window)
            return False
        elif not(self.gender.get()=='Male' or self.gender.get()=='Female'):
            messagebox.showwarning("Empty Field",'Please select gender',parent=self.window)
            return  False
        elif len(self.e4.get())<1:
            messagebox.showwarning("Empty Field",'Please select a valid dob',parent=self.window)
            return False
        elif len(self.e5.get())!=10 or not self.e5.get().isdigit() :
            messagebox.showwarning("Empty Field", 'Please enter a valid phone number', parent=self.window)
            return False
        elif len(self.e6.get())<12 :
            messagebox.showwarning("Empty Field", 'Please enter a valid email', parent=self.window)
            return False
        elif len(self.t1.get(0.0,END))<3:
            messagebox.showwarning("Empty Field", 'Please enter a valid address', parent=self.window)
            return False
        elif self.c1.get() == '--select department--':
            messagebox.showwarning("Empty Field", 'Please select a department', parent=self.window)
            return False
        elif self.c2.get() == '--select job--':
            messagebox.showwarning("Empty Field", 'Please select a job', parent=self.window)
            return False
        elif len(self.e10.get())<2 :
            messagebox.showwarning("Empty Field", 'Please enter your qualification', parent=self.window)
            return False
        elif len(self.t2.get(0.0,END))<5 :
            messagebox.showwarning("Empty Field", 'Please enter your skills', parent=self.window)
            return False
        return True


    dept = []
    def get_department(self,e):
        query = "select * from addjobs "
        row_count =self.curr.execute(query)
        data_list = self.curr.fetchall()

        for value in data_list:
            if value[0] not in self.dept:
                self.dept.append(value[0])
        self.c1.config(values=self.dept)
        if len(self.dept)==0:
            self.c1.set('No department')


    def get_jobs(self,e):
        if len(self.dept)!=0:
            query = "select job_title from addjobs where department = %s"
            row_count = self.curr.execute(query,self.var1.get())
            data_list = self.curr.fetchall()
            jobs = []
            for value in data_list:
                if value[0] not in jobs:
                    jobs.append(value[0])
            self.c2.config(values=jobs)
        else:
            self.c2.set('No job present')


    #-------------------------------clean function for frame ----------------------------
    def clean(self,e):
        self.fetch_widget.delete(0,END)

    def on_enter(self,e):
        self.clear_label.config(fg="#e53935")

    def on_leave(self,e):
        self.clear_label.config(fg="black")

    def b_enter(self, e):
        e.widget.config(bg=self.b_hover)

    def b_leave(self, e):
        e.widget.config(bg=self.b_bg)



if __name__ == '__main__':
    temp = Tk()
    ApplicantClass(temp)
    temp.mainloop()
