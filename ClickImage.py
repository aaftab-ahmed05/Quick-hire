import tkinter
from tkinter import *
import cv2
from tkinter import messagebox
from PIL import Image, ImageTk
from details import app_name


class ClickimageClass:

    def __init__(self, wind):

        self.window = Toplevel(wind)
        self.window.title(app_name + "-Take photo")
        self.ww = self.window.winfo_screenwidth()
        self.wh = self.window.winfo_screenheight()

        # -------------placing window ------------------

        self.window.geometry("%dx%d+%d+%d" % (self.ww//2.5, (self.wh // 1.6), self.ww//3, 75))
        self.window.resizable(False, False)
        self.window.attributes("-topmost",True)
        window_bg = 'skyblue'
        self.window.config(bg=window_bg)


        # ----------------------------------widgets------------------------------------self.

        lab_col_fg = 'black'
        button_bg = '#1E3E62'
        button_fg = 'white'

        # --------------------------------main heading and placement of main heading--------------------------------------

        self.main_heading = Label(self.window, text='Click Picture', fg='black', bg='lightblue',
                                  font=('', 25, 'bold'), borderwidth=5, relief='groove')
        self.main_heading.place(x=0, y=0, relwidth=1, height=55)


        # ------------------------------------------------------buttons and canvas----------------------------------------
        self.wid_h = 50
        my_font = ("Arial",12,"normal")

        self.canvas_w = self.ww//2.5
        self.canvas_h = self.wh//1.6-self.wid_h-55
        self.canvas = tkinter.Canvas(self.window,bg="black")
        self.canvas.place(x=0,y=55,width = self.canvas_w,height=self.canvas_h)

        self.b1 = Button(self.window, text='Click', fg=button_fg, bg=button_bg, font=my_font,command=self.click_image)
        self.b1.place(x=0, y=(self.wh//1.6)-self.wid_h, relwidth=1, height=self.wid_h)

        #--------------------creating capture window-------------------

        self.vid = cv2.VideoCapture(0)
        self.my_cam()


        # -------------calling function that are required------------------------------

        self.window.mainloop()

    # ----------------------------------------------------defining functions-------------------------------------------
    def my_cam(self):
        ret , frame = self.vid.read()
        if ret :
            self.photo = self.create_image(frame)
            self.canvas.create_image(0,0,image=self.photo,anchor=NW)
            self.window.after(30,self.my_cam)

    def create_image(self,frame):
        ret ,frame =self.vid.read()
        if ret:
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame,(int(self.canvas_w),int(self.canvas_h)))
            img = Image.fromarray(frame)
            photo = ImageTk.PhotoImage(image=img)
            return photo

    def click_image(self):
        ret,frame= self.vid.read()
        if ret:
            cv2.imwrite("users_images//captured_image.png", frame)
        self.vid.release()
        self.window.destroy()





if __name__ == '__main__':
    temp = Tk()
    ClickimageClass(temp)
    temp.mainloop()
