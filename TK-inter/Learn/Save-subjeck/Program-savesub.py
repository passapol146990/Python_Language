from tkinter import *
from tkinter import ttk #button beautiful
from tkinter import messagebox

def btn1():
    text='Hello World'
    messagebox.showwarning('Hi',text)
def btn2():
    text='Hello World'
    messagebox.showerror('Hi',text)
def btn3():
    text='Hello World'
    messagebox.showinfo('Hi',text)
def ttk_btn(x,x1,x2):
    return ttk.Button(x,text=x1,command=x2)

gui = Tk()
gui.title('โปรแกรมบันทึกข้อมูล')
gui.geometry('500x400')


lable1 = Label(gui,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
lable1.pack()


b1 = ttk.Button(gui,text='passapol')
b1.pack(ipadx=20,ipady=20)

#ตำแปน่งปุ่ม
b2 = Button(gui,text='passapol')
b2.place(x=0,y=0)

#สร้างกล่อง
fb1 = Frame(gui)
fb1.place(x=50,y=200)
b3 = ttk_btn(fb1,'showwarning',btn1)
b3.pack(ipadx=20,ipady=5)

fb2 = Frame(gui)
fb2.place(x=200,y=200)
b4 = ttk_btn(fb2,'showError',btn2)
b4.pack(ipadx=20,ipady=5)

fb3 = Frame(gui)
fb3.place(x=350,y=200)
b5 = ttk_btn(fb3,'showInfo',btn3)
b5.pack(ipadx=20,ipady=5)


gui.mainloop()