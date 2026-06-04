from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Combobox

import pymysql
from PIL import Image, ImageTk
# import face_recognition
from details import *


class CreateadminClass:

    def __init__(self):


        self.window = Tk()
        self.window.title(app_name + "-Create user")
        ww = 1300
        wh = self.window.winfo_screenheight()

        # -------------placing window ------------------

        self.window.geometry("%dx%d+%d+%d" % (int(ww//2.5)+int(ww*30/100), wh // 1.3, ww//4, 75))
        # self.window.maxsize(, int(wh // 1.3))
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

        wid_font = ("Calibri", 13, 'normal')

        # ----------------------------------widgets------------------------------------

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
        self.c1 = Combobox(self.window,values=['Admin','User'],textvariable=self.var1, state='disable', font=wid_font)
        self.c1.current(0)

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
        # ---------------------------------------------placing widgets-------------------------------------------

        wid_w = 100
        wid_h = 30
        wid_x = (int(ww//2.5)+int(ww*30/100)-330)/2
        wid_y = 80
        diff_x = 130
        diff_y = 60

        # -------------------------------------block 1-------------------------------
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

        # ----------------------------------------------placing buttons-----------------------------------------------

        self.b1.place(x=wid_x + 30, y=wid_y - 40, width=wid_w * 1.3, height=wid_h)
        self.b2.place(x=wid_x + diff_x + 60, y=wid_y - 40, width=wid_w * 1.3, height=wid_h)



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

            # ----------check the face in image------------
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
                    messagebox.showinfo("Success", "Data saved successfully", parent=self.window)
                    un = self.e1.get()
                    self.clear_page()
                    from Homepage import HomeClass
                    self.window.destroy()
                    HomeClass(un,"Admin")

                else:
                    messagebox.showinfo("Failure", "Data not saved ", parent=self.window)

        except Exception as e:
            messagebox.showwarning("Query Error", "Error while executing query :\n" + str(e), parent=self.window)

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

    def b_enter(self, e):
        e.widget.config(bg=self.b_hover)

    def b_leave(self, e):
        e.widget.config(bg=self.b_bg)




if __name__ == '__main__':
    CreateadminClass()
