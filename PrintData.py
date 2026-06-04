from fpdf import FPDF
import webbrowser
import time
from details import *

class PrintClass(FPDF):

    def header(self):
        self.set_font("Arial","",7)
        self.cell(0,0,str(time.ctime()),0,1)
        self.ln(4)
        self.set_font("Arial","B",20)
        self.set_fill_color(119, 201, 242)
        self.cell(0,10,app_name,10,True,"C",fill=True)
        self.ln(20)




    def footer(self):
        self.set_y(-20)
        self.set_font("Arial","",8)
        self.cell(0,3,"Contact:",0,1)
        self.ln(3)
        self.cell(0,3,"Email : quickhire@gamil.com      Phone : 9009867906",0,1)
        self.set_text_color(150, 150, 150)
        self.cell(0,5,"Page no-"+str(self.page_no()),0,0,"C")

    def body(self,heading,data,widths,flag):
        self.add_page()

        self.set_font("Arial", "B", 12)
        if flag == 1:
            self.cell(0, 10, "Recruitment data of the applicants", 0, True, "C")
        elif flag == 2 :
            self.cell(0, 10, "User data", 0, True, "C")
        else:
            self.cell(0, 10, "Available jobs ", 0, True, "C")


        self.set_font("Arial","B",7)
        count = 0

        # ------------------placing headings----------------------------
        for head in heading:
            self.set_fill_color(119, 201, 242)
            self.cell(widths[count] ,5,str(head),1,0,"C",fill=True)
            count+=1
        count = 0
        self.set_font("Arial","",6)
        self.ln(5)

        # ---------------------------placing values-------------------------------------
        for row in data :
            # row = [row[0],row[1],row[2],row[4],row[5],row[7],row[8],row[9],row[10]]
            #-------------------------Recruitment data ------------------------
            if flag == 1:
                for value in row :
                    if value == row[-1]:
                        self.set_font("Arial", "", 5)
                        self.cell(widths[count], 5, str(value), 1, 0)
                    else:
                        self.set_font("Arial", "", 6)
                        self.cell(widths[count], 5, str(value), 1, 0)
                    count+=1

            elif flag == 2:
                for value in row :
                    self.set_font("Arial", "", 6)
                    self.cell(widths[count], 5, str(value), 1, 0,"C")
                    count+=1


            #----------------------------job data------------------------
            else:
                for value in row :
                    self.set_font("Arial", "", 7)
                    self.cell(widths[count],5,str(value),1,0)
                    count+=1
            count = 0
            self.ln(5)


if __name__ == '__main__':
    pdf = PrintClass()
    widths =[10,22,14,18,35,18,27,16,30]
    print(sum(widths))
    heading = ["ID","Name","DOB","Phone","Email","Department","Job Selected","Qualification","Skills"]
    data = [(1001, 'aman', "2000-7-20", 9854621354, 'aman@gmail.com', 'Marketing', 'Advertisement creator', 'BCA', 'video editor\n'),(1001, 'aman', "2000-7-20", 9854621354, 'aman@gmail.com', 'Marketing', 'Advertisement creator', 'BCA', 'video editor\n'),(1001, 'aman', "2000-7-20", 9854621354, 'aman@gmail.com', 'Marketing', 'Advertisement creator', 'BCA', 'video editor\n'),(1001, 'aman', "2000-7-20", 9854621354, 'aman@gmail.com', 'Marketing', 'Advertisement creator', 'BCA', 'video editor\n'),]
    pdf.body(heading,data,widths,1)
    pdf.output("mypdf.pdf")
    webbrowser.open("mypdf.pdf")
