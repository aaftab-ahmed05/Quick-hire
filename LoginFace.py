from tkinter import *
import numpy as np
from tkinter import messagebox
from PIL import Image,ImageTk
import os
from details import *
import pymysql
import cv2
import face_recognition

class LoginfaceClass:
    folder = "users_images"

    def __init__(self):
        self.window = Tk()
        self.window.title(app_name + "-Login")
        logoimg = Image.open("assets//logo.png")
        logopic = ImageTk.PhotoImage(logoimg)
        self.window.iconphoto(True, logopic)
        self.ww = self.window.winfo_screenwidth()
        self.wh = self.window.winfo_screenheight()

        # -------------placing window ------------------

        self.window.geometry("%dx%d+%d+%d" % (self.ww // 2.2, (self.wh // 1.6+70), self.ww // 3.5, 75))
        self.window.resizable(False, False)
        self.window.attributes("-topmost", True)

        # ----------------------------------widgets------------------------------------self.

        heading_bg = "#2D3748"
        heading_fg = "#E2E8F0"
        window_bg = '#2D3748'
        lab_col_fg = '#FFFFFF'
        self.b_bg = "#222222"
        b_fg = "#F0F0F0"
        self.b_hover = "#3C5A78"
        self.window.config(bg=window_bg)

        # --------------------------------main heading and placement of main heading------------------------------------

        self.main_heading = Label(self.window, text='Face Login', fg=heading_fg, bg=heading_bg,
                                  font=('Calibri', 25, 'bold'), borderwidth=5, relief='groove')
        self.main_heading.place(x=0, y=0, relwidth=1, height=55)

        # ------------------------------------------------------buttons and canvas--------------------------------------

        self.wid_h = 50
        my_font = ("Calibri", 12, "normal")
        self.canvas_w = self.ww // 2
        self.canvas_h = self.wh // 1.6 - self.wid_h - 55
        self.canvas = Canvas(self.window, bg="black")
        self.canvas.place(x=0, y=55, width=self.canvas_w, height=self.canvas_h)
        self.b1 = Button(self.window, text='Detect face', fg=b_fg, bg=self.b_bg, font=("Calibri",18,""),
                         command=self.check_face)
        self.b1.place(x=0, y=(self.wh // 1.6) - self.wid_h+20, relwidth=1, height=self.wid_h)
        self.b1.bind("<Enter>",self.b_enter)
        self.b1.bind("<Leave>",self.b_leave)

        self.another_way = Label(self.window, text='Login using username and password...', fg="grey", bg=window_bg,
                                 font=('Calibri', 15, 'normal'))
        self.another_way.bind("<Enter>", self.on_enter)
        self.another_way.bind("<Leave>", self.on_leave)
        self.another_way.place(x=0,y=(self.wh // 1.6)+20 ,relwidth=1,height=self.wid_h-10)
        self.another_way.bind("<Button-1>", self.login_using_pass)
        self.info = Label(self.window,bg='black',anchor="center")
        self.info.place(x=0,y=(self.wh // 1.6) - self.wid_h,relwidth=1,height=20 )

        # --------------------creating capture window-------------------

        images_list = os.listdir(self.folder)
        self.known_face_encoding = []
        self.known_faces_names = []
        for img_name in images_list:
            print(img_name)
            selected_image = face_recognition.load_image_file(self.folder + "/" + img_name)
            s_encoding = face_recognition.face_encodings(selected_image)
            if not s_encoding:
                continue  # skip if given image is not recoginizable
            selected_encoding = s_encoding[0]
            self.known_face_encoding.append(selected_encoding)
            # self.known_faces_names.append(img_name.split(".")[0])
            self.known_faces_names.append(img_name)
        # print("All Names List = ", self.known_faces_names)


        # -------------calling function that are required------------------------------

        self.vid = cv2.VideoCapture(0)
        self.my_cam()

        self.connect_db()
        self.window.mainloop()

    # ----------------------------------------------------defining functions-------------------------------------------

    def my_cam(self):
        ret, frame = self.vid.read()
        if ret:
            self.photo = self.create_image(frame)
            self.canvas.create_image(0, 0, image=self.photo, anchor=NW)
            self.canvas.image = self.photo
            self.window.after(30, self.my_cam)

    def create_image(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (int(self.canvas_w), int(self.canvas_h)))
        img = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image=img)
        return photo

    # def click_image(self):
    #     ret, frame = self.vid.read()
    #     if ret:
    #         cv2.imwrite("users_images//captured_image.png", frame)
    #     self.vid.release()
    #     self.window.destroy()

    def check_face(self):
            ret ,frame = self.vid.read()
            recent_face_location = face_recognition.face_locations(frame)
            recent_face_encoding = face_recognition.face_encodings(frame,recent_face_location)
            for face_encoding in recent_face_encoding:
                matches = face_recognition.compare_faces(self.known_face_encoding,face_encoding)
                name = ''
                face_distance = face_recognition.face_distance(self.known_face_encoding,face_encoding)
                best_match = np.argmin(face_distance)
                if matches[best_match]:
                    name = self.known_faces_names[best_match]
                    if name in self.known_faces_names:
                        self.info.config(text = "Face found",fg = "lightgreen")
                        self.img_name = name
                        self.check_data()
                        return
            self.info.config(text= "Unknown face",fg = "red")

    def connect_db(self):
        try:
            self.conn = pymysql.connect(host=myhost, user=myuser, password=mypassword, database=mydb)
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error", "Error while connecting to the database :\n" + str(e),
                                 parent=self.window)

    def check_data(self):
        # username password user_type user_image
        try:
            query = "select * from users where user_image=%s"
            row_count = self.curr.execute(query,(self.img_name))
            data = self.curr.fetchone()
            if data[-1]==self.img_name :
                un = data[0]
                ut = data[2]
                messagebox.showinfo("Success","You are logged in ",parent= self.window)
                from Homepage import HomeClass
                self.close()
                HomeClass(un,ut)
            else:
                messagebox.showerror("Empty ","User does not exist",parent=self.window)
        except Exception as e:
            messagebox.showerror("Query Error ","Error while confirming the data :\n"+str(e),parent=self.window)

    def close(self):
        self.vid.release()
        self.window.destroy()

    def login_using_pass(self,e):
        from LoginText import LogintextClass
        self.close()
        LogintextClass()

    def on_enter(self, e):
        self.another_way.config(fg="white",font=('Calibri',17,'bold'))

    def on_leave(self, e):
        self.another_way.config(fg="grey",font=('Calibri',17,'bold'))

    def b_enter(self, e):
        e.widget.config(bg=self.b_hover)

    def b_leave(self, e):
        e.widget.config(bg=self.b_bg)

if __name__ == '__main__':

    LoginfaceClass()
