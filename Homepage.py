from tkinter import *
from PIL import Image,ImageTk
import time
from ChangePassword import ChangepasswordClass
from CreateUser import CreateuserClass
from UserData import UserDataClass
from details import *
from Applicant import ApplicantClass
from Addjobs import AddjobsClass
from RecruitmentData import RecruitmentDataClass
from JobData import JobDataClass


class HomeClass:
    def __init__(self,un,ut):
        self.username = un
        self.window = Tk()
        self.window.title(app_name)
        self.w=self.window.winfo_screenwidth()
        self.h=self.window.winfo_screenheight()-125

        self.window.title(app_name)
        logoimg = Image.open("assets//logo.png")
        logopic = ImageTk.PhotoImage(logoimg)
        self.window.iconphoto(True,logopic)
        self.window.geometry("%dx%d+%d+%d" % (self.w//2,self.h//2,self.w//4,self.h//4))
        self.window.minsize(400,300)
        self.window.state("zoomed")
        self.window.protocol("WM_DELETE_WINDOW", self.logout)

        self.window.config(bg="black")

        #--------------------------------------colours--------------------------------------
        heading_bg = "#2D3748"
        heading_fg = "#E2E8F0"
        frame_bg =  '#2D3748'
        self.b_bg = "#222222"
        b_fg = "#F0F0F0"
        self.b_hover = "#3C5A78"
        #---------------------------------------main heading and background image------------------------------------

        self.main_heading = Label(self.window ,text="Welcome To "+app_name,font=("Calibri",25,"bold") ,bg=heading_bg,fg=heading_fg,borderwidth=5,relief='groove')
        self.main_heading.place(x=0,y=0,width=self.w,height=55)
        self.image_loc='assets//background.png'
        self.bg_img=ImageTk.PhotoImage(Image.open(self.image_loc).resize((self.w-225,self.h)))
        self.bg_label=Label(self.window,image=self.bg_img,compound=CENTER)
        self.bg_label.place(x=220,y=54)

        #------------------------------------------------frame and buttons--------------------------------------------

        f_wid = 220
        my_font = "Calibri",11,'bold'

        #-----------------------------------------------------------frame----------------------------------------------

        self.f1=Frame(self.window,bg=frame_bg)
        self.f1.place(x=0,y=55,width=f_wid,height=self.h)
        # self.f1.config(bg="pink")
        # self.f1.place(x=0,y=30,width=w,height=f_hei)

        #-------------------------------------------------buttons and button images------------------------------------
        b_wid = 170
        b_hei = 40
        b_y = 80
        y_diff = 70
        img_size = 30

        self.type_label = Label(self.f1, text="Login at : "+str(time.ctime())[11:19]+"\n"+"Login type : "+ut+" ",font=("Arial",12,"normal"),fg="white",bg=frame_bg)

        self.b1_img=ImageTk.PhotoImage(Image.open("assets/applicant.png").resize((img_size, img_size)))
        self.b1=Button(self.f1,text='''  Applicant's Profile''',font=my_font ,anchor="w",bg=self.b_bg,fg=b_fg,image=self.b1_img,compound=LEFT,command=lambda : ApplicantClass(self.window))
        self.b1.bind("<Enter>", lambda e:self.on_enter(e))
        self.b1.bind("<Leave>", self.on_leave)
        self.b2_img=ImageTk.PhotoImage(Image.open("assets/addjobs.png").resize((img_size,img_size)))
        self.b2=Button(self.f1,text='  Add Jobs',font=my_font,anchor="w",bg=self.b_bg,fg=b_fg,image=self.b2_img,compound=LEFT ,command=lambda : AddjobsClass(self.window))
        self.b2.bind("<Enter>", self.on_enter)
        self.b2.bind("<Leave>", self.on_leave)
        self.b3_img=ImageTk.PhotoImage(Image.open("assets/user.png").resize((img_size, img_size)))
        self.b3=Button(self.f1,text='  Create user',font=my_font,anchor="w",bg=self.b_bg,fg=b_fg,image=self.b3_img,compound=LEFT ,command=lambda : CreateuserClass(self.window))
        self.b3.bind("<Enter>", self.on_enter)
        self.b3.bind("<Leave>", self.on_leave)
        self.b4_img=ImageTk.PhotoImage(Image.open("assets//recruitment.png").resize((img_size,img_size)))
        self.b4=Button(self.f1,text='  Recruitment Data',font=my_font,anchor="w",bg=self.b_bg,fg=b_fg,image=self.b4_img,compound=LEFT,command=lambda:RecruitmentDataClass(self.window))
        self.b4.bind("<Enter>", self.on_enter)
        self.b4.bind("<Leave>", self.on_leave)
        self.b5_img=ImageTk.PhotoImage(Image.open("assets/job list.png").resize((img_size, img_size)))
        self.b5=Button(self.f1,text='  Job List',font=my_font,anchor="w",bg=self.b_bg,fg=b_fg,image=self.b5_img,compound=LEFT,command= lambda :JobDataClass(self.window))
        self.b5.bind("<Enter>", self.on_enter)
        self.b5.bind("<Leave>", self.on_leave)
        self.b6_img=ImageTk.PhotoImage(Image.open("assets//userdata.png").resize((img_size,img_size)))
        self.b6=Button(self.f1,text='  User Data',bg=self.b_bg,fg=b_fg,font=my_font,anchor="w",image=self.b6_img,compound=LEFT,command=lambda :UserDataClass(self.window))
        self.b6.bind("<Enter>", self.on_enter)
        self.b6.bind("<Leave>", self.on_leave)
        self.b7_img=ImageTk.PhotoImage(Image.open("assets//gear.png").resize((img_size,img_size)))
        self.b7=Button(self.f1,text='  Change Password',font=my_font,anchor="w",bg=self.b_bg,fg=b_fg,image=self.b7_img,compound=LEFT,command=lambda :ChangepasswordClass(self.window,self.username))
        self.b7.bind("<Enter>",  self.on_enter)
        self.b7.bind("<Leave>",  self.on_leave)
        self.b8_img=ImageTk.PhotoImage(Image.open("assets//logout.png").resize((img_size,img_size)))
        self.b8=Button(self.f1,text='   Logout',font=my_font,anchor="w",bg=self.b_bg,fg=b_fg,image=self.b8_img,compound=LEFT,command=self.logout)
        self.b8.bind("<Enter>",  self.on_enter)
        self.b8.bind("<Leave>",  self.on_leave)
        self.b9_img=ImageTk.PhotoImage(Image.open("assets//i.png").resize((img_size,img_size)))
        self.b9=Button(self.f1,text='   About',font=my_font,anchor="w",bg=self.b_bg,fg=b_fg,image=self.b9_img,compound=LEFT,command=self.open_website)
        self.b9.bind("<Enter>",  self.on_enter)
        self.b9.bind("<Leave>",  self.on_leave)

        self.type_label.place(x=(f_wid-b_wid)/2,y=10)
        self.b1.place(width=b_wid,height=b_hei,x=(f_wid-b_wid)/2,y=b_y)
        b_y+=y_diff
        self.b2.place(width=b_wid,height=b_hei,x=(f_wid-b_wid)/2,y=b_y)
        b_y += y_diff

        self.b3.place(width=b_wid,height=b_hei,x=(f_wid-b_wid)/2,y=b_y)
        b_y += y_diff
        self.b4.place(width=b_wid,height=b_hei,x=(f_wid-b_wid)/2,y=b_y)
        b_y += y_diff
        self.b5.place(width=b_wid,height=b_hei,x=(f_wid-b_wid)/2,y=b_y)
        b_y += y_diff
        if ut == 'Admin':
            self.b6.place(width=b_wid, height=b_hei,x=(f_wid - b_wid) / 2, y=b_y)
            b_y += y_diff
        self.b7.place(width=b_wid, height=b_hei,x=(f_wid - b_wid) / 2, y=b_y)
        b_y += y_diff
        self.b8.place(width=b_wid, height=b_hei,x=(f_wid - b_wid) / 2, y=b_y)
        b_y += y_diff
        self.b9.place(width=b_wid, height=b_hei, x=(f_wid - b_wid) / 2, y=b_y)
        b_y += y_diff
        if ut == "User":
            self.b3.config(state="disabled")
            self.b3.bind("<Button>",lambda e : self.b3.config(text="  Login as Admin first",font=("Calibri",11,"bold"),bg="#e53935"))

        self.window.mainloop()

    #---------------------------------------------------functions------------------------------------------------------
    count = 0
    def change_theme(self):
        if self.count%2==0:
            self.bg_img=ImageTk.PhotoImage(Image.open('assets//homepage2dark.png').resize((self.w-185,self.h-120)))
            self.bg_label.config(image=self.bg_img)
            self.main_heading.config(bg="#222831", fg='white')
            self.f1.config(bg='#393E46')
            self.b7.config(text='Light Theme')
            self.count += 1
        else:
            self.bg_img = ImageTk.PhotoImage(Image.open('assets//homepage.png').resize((self.w-185,self.h-120)))
            self.bg_label.config(image=self.bg_img)
            self.main_heading.config(bg="light blue",fg='black')
            self.f1.config(bg='#e3e7e8')
            self.b7.config(text='Dark Theme')
            self.count-=1

    def on_enter(self,e):
        e.widget.config(bg=self.b_hover)

    def on_leave(self,e):
        e.widget.config(bg=self.b_bg)

    def logout(self):
        self.window.destroy()
        from LoginText import LogintextClass
        LogintextClass()

    def open_website(self):
        import webbrowser
        import os
        file_path = os.path.abspath("index.html")
        print(file_path)
        webbrowser.open(f"file:///{file_path}")

if __name__ == '__main__' :

    HomeClass('abc','Admin')

