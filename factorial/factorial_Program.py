import tkinter as tk
import colorama
def Home():
    home = tk.Tk()
    home.minsize(width=400,height=600)
    home.title("Factoria carculate")
    title1 = tk.Label(master=home,text="เลือกสูตรที่ต้องการ",font=20)
    title1.pack()
    menu1 = tk.Button(master=home,text="n! or Pn!",font=10,command=creat_window)
    menu1.pack()
    menu2 = tk.Button(master=home,text="Pn,r! or Pn-r!",font=10)
    menu2.pack()
    home.mainloop()

def creat_window(self,number):
    #สร้างหน้าจอ
    window = tk.Tk()
    window.title("Factoria")
    window.minsize(height=400, width=300)
    lable = tk.Label(master=window,text="Factoria")
    lable.pack()
    #ช่องใส่เลข
    entry = tk.Entry(master=window)
    entry.pack()
    #ปุ่มกด
    button = tk.Button(master=window,text="ok", height=2, width=4,command=oc)
    button.pack()
    num = int(entry.get())
    oc(num)
    #แสดงข้อมูล
    lable = tk.Label(master=window,text=number)
    lable.pack()
    window.mainloop()

def oc(self,number):
    number = int(number)+1
    f =1
    for i in range(1,number):
        f = f * i
    creat_window(f)

Home()
