from logging import root
from tkinter import*
import qrcode
from PIL import Image,ImageTk
import resizeimage
from resizeimage import resizeimage
from turtle import title
from xml.dom.minidom import Entity
class Qr_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Generator by me")
        self.root.resizable(False,False)
        
        title=Label(self.root,text="QR Code Generator ",font=("times new roman",35),bg='magenta').place(x=0,y=0,relwidth=1)
        
        #--------------------------------Employee Details windows---------------------------
        #----------------------variables-------------------------------
        self.var_emp_code=StringVar()
        self.var_name=StringVar()
        self.var_department=StringVar()
        self.var_designation=StringVar()
        
        emp_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        emp_Frame.place(x=50,y=100,width=500,height=380)
        
        emp_title=Label(emp_Frame,text="            Employee Deatails",font=("goudy old style",20),bg='gold',anchor='w').place(x=0,y=0,relwidth=1)
        
        lbl_emp_title=Label(emp_Frame,text="Employee ID",font=("time new roman",15,'bold'),bg='white').place(x=10,y=100)
        lbl_name=Label(emp_Frame,text="Name",font=("time new roman",15,'bold'),bg='white').place(x=10,y=140)
        lbl_department=Label(emp_Frame,text="Department",font=("time new roman",15,'bold'),bg='white').place(x=10,y=180)
        lbl_designation=Label(emp_Frame,text="Designation",font=("time new roman",15,'bold'),bg='white').place(x=10,y=220)
        
        txt_emp_code=Entry(emp_Frame,font=("time new roman",15),textvariable=self.var_emp_code,bg='lightblue').place(x=200,y=100)
        txt_name=Entry(emp_Frame,font=("time new roman",15),textvariable=self.var_name,bg='#AF69EE').place(x=200,y=140)
        txt_department=Entry(emp_Frame,font=("time new roman",15),textvariable=self.var_department,bg='lightgreen').place(x=200,y=180)
        txt_designation=Entry(emp_Frame,font=("time new roman",15),textvariable=self.var_designation,bg='lightpink').place(x=200,y=220)
        
        btn_generate=Button(emp_Frame,text='QR Generate',command=self.generate,font=("times new roman",18,'bold'),bg='red',fg='white').place(x=11,y=270,width=200,height=30)
        btn_clear=Button(emp_Frame,text='Clear',command=self.clear,font=("times new roman",18,'bold'),bg='green',fg='white').place(x=223,y=270,width=200,height=30)
        
        self.msg=''
        self.lbl_msg=Label(emp_Frame,text=self.msg,font=("times new roman",20,'bold'),bg='white',fg='green')
        self.lbl_msg.place(x=0,y=320,relwidth=1)
        
        #<------------------employee QR code window-------------------->
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=600,y=100,width=235,height=380)
        
        emp_title=Label(qr_Frame,text="Employee Qr code",font=("goudy old style",20),bg='gold',fg='black').place(x=0,y=0)
        
        self.qr_code=Label(qr_Frame,text='No Qr\nAvailible',font=('times new roman',15),bg='#200c3a',fg='white',relief=RIDGE)
        self.qr_code.place(x=28,y=100,width=180,height=180)
    
    def clear(self):
        self.var_emp_code.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_designation.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')
    def generate(self):
        if self.var_designation.get()=='' or self.var_emp_code.get()=='' or self.var_department.get()=='' or self.var_name.get()=='':
            self.msg='All fields are Required!!!'
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Employ Id:{self.var_emp_code.get()} \nEmployee name:{self.var_name.get()} \nDepartment:{self.var_department.get()} \nDesignation:{self.var_designation.get()}")
            qr_code=qrcode.make(qr_data)
           # print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            #----------------QR code Image Upade--------------------------------
            self.im=ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)
            #--------------updating notifications-----------------------
            self.msg='QR Genereted succdssfully!!!!'
            self.lbl_msg.config(text=self.msg,fg='green')
root=Tk()
obj=Qr_Generator(root)
root.mainloop()
