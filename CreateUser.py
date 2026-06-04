from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox

import pymysql
from PIL import Image, ImageTk
# import face_recognition
from details import *


class CreateuserClass:

    def __init__(self, wind):


        self.window = Toplevel(wind)
        self.window.title(app_name + "-Create user")
        ww = 1300
        wh = self.window.winfo_screenheight()

        # -------------placing window ------------------

        self.window.geometry("%dx%d+%d+%d" % (1300, wh // 1.3, ww//4, 75))
        self.window.maxsize(int(ww//2.5)+int(ww*30/100), int(wh // 1.3))
        self.window.resizable(False, False)

        # ------------------------------------colours-------------------------------
        heading_bg = "#2D3748"
        heading_fg = "#E2E8F0"
        window_bg = '#2D3748'
        lab_col_fg = '#FFFFFF'
        self.b_bg = "#222222"
        b_fg = "#F0F0F0"
        self.b_hover = "#3C5A78"
        self.window.config(bg=window_bg)

        #------------------------------------frame creation and placing------------------------------------

        frame_width = ww*30/100
        frame_height = wh-55
        self.f1 = Frame(self.window)
        self.f1.place(x=ww//2.5,y=55,width=ww*30/100,height=wh-55)

        self.f_heading = Label(self.f1,text="Manage Data",font=('Calibri',18,'normal'))
        self.f_heading.place(x=0,y=10,relwidth=1,height=30)


        # ----------------------------------widgets------------------------------------

        wid_font = ("Calibri", 13, 'normal')


        # --------------------------------main heading and placement of main heading--------------------------------------

        self.main_heading = Label(self.window, text='Create New User', fg=heading_fg, bg=heading_bg,
                                  font=('Calibri', 25, 'bold'), borderwidth=5, relief='groove')
        self.main_heading.place(x=0, y=0, relwidth=1, height=55)

        # --------------------------------------------widgets creation---------------------------

        self.l1 = Label(self.window, text='Username', fg=lab_col_fg, bg=window_bg, font=wid_font, anchor='w')
        self.l2 = Label(self.window, text='Password', fg=lab_col_fg, bg=window_bg, font=wid_font, anchor='w')
        self.l3 = Label(self.window, text='User type', fg=lab_col_fg, bg=window_bg, font=wid_font, anchor='w')
        self.l4 = Label(self.window, text="Add image" , fg=lab_col_fg, bg=window_bg, font=wid_font, anchor='w')

        self.imglabel = Label(self.window, borderwidth=2.5, relief='sunken')
        self.imglabel.bind('<Button-1>', lambda e: self.set_profile_img(e))

        self.e1 = Entry(self.window, font=wid_font)
        self.e2 = Entry(self.window, font=wid_font)
        self.var1 = StringVar()
        self.c1 = Combobox(self.window,values=['Admin','User'],textvariable=self.var1, state='readonly', font=wid_font)
        self.c1.set(value='--select usertype--')

        # ------------------------------------------------------buttons----------------------------------------

        #------------window----------------

        self.b1 = Button(self.window, text='Save', fg=b_fg, bg=self.b_bg, font=wid_font, command=self.save_data_db)
        self.b1.bind("<Enter>", self.b_enter)
        self.b1.bind("<Leave>", self.b_leave)
        self.b2 = Button(self.window, text='Reset',fg=b_fg, bg=self.b_bg, font=wid_font, command=self.clear_page)
        self.b2.bind("<Enter>", self.b_enter)
        self.b2.bind("<Leave>", self.b_leave)
        self.capture_button = Button(self.window, text='Capture Image', fg=b_fg, bg=self.b_bg, font=wid_font,command=self.open_click_image)
        self.capture_button.bind("<Enter>", self.b_enter)
        self.capture_button.bind("<Leave>", self.b_leave)
        #-------------frame----------------

        self.b3 = Button(self.f1, text='Fetch Data', fg=b_fg, bg=self.b_bg, font=wid_font,command=self.fetch_data_db)
        self.b3.bind("<Enter>", self.b_enter)
        self.b3.bind("<Leave>", self.b_leave)
        self.b4 = Button(self.f1, text='Update Data', fg=b_fg, bg=self.b_bg, font=wid_font,command=self.update_data_db)
        self.b4.bind("<Enter>", self.b_enter)
        self.b4.bind("<Leave>", self.b_leave)
        self.b5 = Button(self.f1, text='Delete Data', fg=b_fg, bg=self.b_bg, font=wid_font,command=self.delete_data_db)
        self.b5.bind("<Enter>", self.b_enter)
        self.b5.bind("<Leave>", self.b_leave)

        # ---------------------------------------------placing widgets-------------------------------------------

        wid_w = 100
        wid_h = 30
        wid_x = 30
        wid_y = 80
        diff_x = 130
        diff_y = 60

        self.imgsize = 175
        self.default_name = 'default.png'
        self.actual_name = 'default.png'
        self.default = ImageTk.PhotoImage(Image.open("users_images//" + self.default_name).resize((self.imgsize+50, self.imgsize)))

        self.l1.place(x=wid_x, y=wid_y, width=wid_w, height=wid_h)
        self.e1.place(x=wid_x + diff_x, y=wid_y, width=wid_w * 2, height=wid_h)
        wid_y += diff_y
        self.l2.place(x=wid_x, y=wid_y, width=wid_w, height=wid_h)
        self.e2.place(x=wid_x + diff_x, y=wid_y, width=wid_w * 2, height=wid_h)
        wid_y += diff_y
        self.l3.place(x=wid_x, y=wid_y, width=wid_w, height=wid_h)
        self.c1.place(x=wid_x + diff_x, y=wid_y, width=wid_w * 2, height=wid_h)
        wid_y += diff_y
        self.l4.place(x=wid_x, y=wid_y+diff_y, width=wid_w, height=wid_h)
        self.imglabel.config(image=self.default)
        self.imglabel.place(x=wid_x + diff_x, y=wid_y, width=self.imgsize+50, height=self.imgsize)
        wid_y+=diff_y*3
        self.capture_button.place(x=wid_x+diff_x, y=wid_y,width=self.imgsize+50,height=wid_h)
        wid_y += diff_y
        wid_y += diff_y

        # ----------------------------------------------placing buttons outside the frame -----------------------------------------------

        self.b1.place(x=wid_x + 30, y=wid_y - 40, width=wid_w * 1.3, height=wid_h)
        self.b2.place(x=wid_x + diff_x + 60, y=wid_y - 40, width=wid_w * 1.3, height=wid_h)

        # --------------------------------------creating widgets for frame and adding buttons--------------------------

        # ---------------widgets creation and placing-----------------------------
        self.info_label = Label(self.f1, text="Enter username below to manage the data", fg='gray',
                                font=wid_font)
        self.info_label.place(x=0, y=50, relwidth=1)
        self.framelabel = Label(self.f1, text="Username :", font=('Calibri', 12, 'bold'))
        self.fetch_widget = Entry(self.f1, font=wid_font)
        self.framelabel.place(x=frame_width / 4, y=150, width=wid_w + 20, height=wid_h)
        self.fetch_widget.place(x=frame_width / 4 + diff_x, y=150, width=wid_w, height=wid_h)
        self.clear_label = Label(self.f1, text='clear', font=('Calibri', 11, 'normal'))
        self.clear_label.bind("<Button-1>", self.clean)
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
        self.window.bind("<FocusIn>",lambda e:self.place_image())
        self.flag = False
        self.window.mainloop()


    # ----------------------------------------------------defining functions-------------------------------------------

    def connect_db(self):
        try:
            self.conn = pymysql.connect(host=myhost, user=myuser, password=mypassword, database=mydb)
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error", "Error while connecting to the database :\n" + str(e),
                                 parent=self.window)

    def set_profile_img(self, e):
        filename = askopenfilename(
            filetypes=[('Pictures', '*.jpg;*.png;*.jpeg'), ('PNG Images', '*.png'), ('JPG Images', "*.jpg")],
            parent=self.window)
        if filename != '':

            self.profileimg = Image.open(filename).resize((self.imgsize+50, self.imgsize))
            self.profilepic = ImageTk.PhotoImage(self.profileimg)
            self.imglabel.config(image=self.profilepic)
            #
            # image = face_recognition.load_image_file(filename)
            # face_locations = face_recognition.face_locations(image)
            # if len(face_locations) != 1:
            #     messagebox.showwarning("Input Error", "Please select an image with a face", parent=self.window)
            #     self.actual_name = self.default_name
            #     self.profileimg = Image.open("users_images//" + self.actual_name).resize((self.imgsize + 50, self.imgsize))
            #     self.profilepic = ImageTk.PhotoImage(self.profileimg)
            #     self.imglabel.config(image=self.profilepic)

            filename = filename.split('/')[-1]
            import time
            add_time = time.time()
            self.actual_name = (str(int(add_time)))[5:] + filename



        else:
            messagebox.showwarning("Image Missing", "Profile image not selected.", parent=self.window)

    def open_click_image(self):
        self.flag = True
        from ClickImage import ClickimageClass
        ClickimageClass(self.window)

    def place_image(self):
        if self.flag == True:
            self.flag = False

            filename = "captured_image.png"
            self.profileimg = Image.open("users_images//" + filename).resize((self.imgsize + 50, self.imgsize))
            self.profilepic= ImageTk.PhotoImage(self.profileimg)
            self.imglabel.config(image = self.profilepic)

            import time
            add_time = str(int(time.time()))[5:]
            self.actual_name = add_time + filename

            # # ----------check the face in image------------
            # image = face_recognition.load_image_file("users_images//"+filename)
            # face_locations = face_recognition.face_locations(image)
            # if len(face_locations)!=1:
            #     messagebox.showwarning("Input Error","Please select an image with a face",parent=self.window)
            #     self.actual_name = self.default_name
            #     self.profileimg = Image.open("users_images//"+self.actual_name).resize((self.imgsize+50,self.imgsize))
            #     self.profilepic = ImageTk.PhotoImage(self.profileimg)
            #     self.imglabel.config(image=self.profilepic)

    def save_data_db(self):

        try:
            # username password user_type user_image

            if self.required_info():

                query = "insert into users values(%s,%s,%s,%s)"
                row_count = self.curr.execute(query,(self.e1.get(), self.e2.get(),self.var1.get(),self.actual_name))
                self.conn.commit()

                if row_count == 1:
                    if self.actual_name != self.default_name:
                        self.profileimg.save("users_images//" + self.actual_name)
                        import os
                        if "captured_image.png" in os.listdir("users_images"):
                            os.remove("users_images//captured_image.png")

                    self.clear_page()
                    messagebox.showinfo("Success", "Data saved successfully", parent=self.window)

                else:
                    messagebox.showinfo("Failure", "Data not saved ", parent=self.window)

        except Exception as e:
            messagebox.showwarning("Query Error", "Error while executing query :\n" + str(e), parent=self.window)

    def fetch_data_db(self):
        try:
            query = "select * from users where username=%s"
            row_count = self.curr.execute(query, self.fetch_widget.get())
            data = self.curr.fetchone()
            self.clear_page()
            self.e1.insert(0, data[0])
            self.e2.insert(0, data[1])
            self.var1.set(data[2])
            self.oldname = data[3]
            self.actual_name = data[3]
            self.profileimg = Image.open("users_images//" + self.actual_name).resize((self.imgsize+50, self.imgsize))
            self.profilepic = ImageTk.PhotoImage(self.profileimg)
            self.imglabel.config(image=self.profilepic)

            if row_count == 1:
                messagebox.showinfo("Success", "Data Fetched successfully", parent=self.window)
            else:
                messagebox.showinfo("Failure", "Data not Fetched ", parent=self.window)

        except Exception as e:
            messagebox.showwarning("Query Error", "Error while executing query :\n" + str(e), parent=self.window)
            print(e)

    def update_data_db(self):
        #                               username password user_type user_image

        try:
            if self.required_info():
                query = "update users set password=%s,user_type=%s, user_image=%s where username = %s"
                row_count = self.curr.execute(query,(self.e2.get(), self.var1.get(),self.actual_name, self.e1.get()))
                self.conn.commit()

                if row_count == 1:
                    messagebox.showinfo("Success", "Data updated successfully", parent=self.window)
                    if self.actual_name != self.oldname:
                        self.profileimg.save('users_images//' + self.actual_name)
                        if self.oldname != self.default_name:
                            import os
                            os.remove("users_images//" + self.oldname)

                    self.clear_page()

                else:
                    messagebox.showinfo("Failure", "Data not updated ", parent=self.window)

        except Exception as e:
            messagebox.showwarning("Query Error", "Error while executing query :\n" + str(e), parent=self.window)

    def delete_data_db(self):

        try:
            query = "delete from users where username=%s"
            row_count = self.curr.execute(query, self.fetch_widget.get())

            ans = messagebox.askquestion("Confirmation", "Do you really want to delete the data ?", parent=self.window)
            if ans == 'yes':
                self.conn.commit()
                self.clear_page()
                if row_count == 1:
                    if self.actual_name != self.default_name:
                        import os
                        os.remove('users_images//' + self.actual_name)

                    messagebox.showinfo("Success", 'Data deleted Successfully', parent=self.window)
                else:
                    messagebox.showwarning("Failure", 'Data not deleted', parent=self.window)


        except Exception as e:
            messagebox.showerror("Query Error", "Error while executing query :\n" + str(e), parent=self.window)

    def clear_page(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.var1.set("--select usertype--")
        self.imglabel.config(image=self.default,relief='sunken')

        # self.actual_name='default.png'

    def required_info(self):
        if len(self.e1.get()) < 4 or not self.e1.get().isalnum():
            messagebox.showwarning("Empty Field", 'Username atleast contain 4 characters', parent=self.window)
            return False
        elif len(self.e2.get()) < 4:
            messagebox.showwarning("Empty Field", 'Password atleast contain 4 characters', parent=self.window)
            return False
        elif self.var1.get() == '--select usertype--':
            messagebox.showwarning("Empty Field", 'Please select user type', parent=self.window)
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
    CreateuserClass(temp)
    temp.mainloop()
