from tkinter import*
def showwindow():
    window = Tk()
    window.title("factoria")
    window.minsize(width=400,height=600)
    title = Label(text="เลือกฟังก์ชันที่ต้องการ",font=60)
    title.pack()
    button1 = Button(master=window,text="Pn!",font=20,command=Pn)
    button1.pack()
    button2 = Button(master=window, text="Pn-r!", font=20, command=Pnr)
    button2.pack()

    window.mainloop()
def Pn():
    window = Tk()
    window.title("Pn!")
    window.minsize(width=400,height=500)

    lable = Label(master=window,text="Pn!",font=20)
    lable.pack()
    entry = Entry(master=window)
    entry.pack()
    def cal():
        num = int(entry.get()) + 1
        f = 1
        for i in range(1,num):
            f *=i
        lableshow.configure(text=f,font=20)
    button = Button(command=cal,master=window,text="ok",font=20)
    button.pack()
    lableshow = Label(master=window)
    lableshow.pack()
    window.mainloop()
def Pnr():
    window = Tk()
    window.title("Pn-r!")
    window.minsize(width=400,height=500)

    lable = Label(master=window,text="Pn-r!",font=20)
    lable.pack()
    entry1 = Entry(master=window)
    entry1.pack()
    entry2 = Entry(master=window)
    entry2.pack()
    def cal():
        num = int(entry1.get()) - int(entry2.get())
        f = 1
        for i in range(1,num + 1):
            f *=i
        lableshow.configure(text=f,font=20)
    button = Button(command=cal,master=window,text="ok",font=20)
    button.pack()
    lableshow = Label(master=window)
    lableshow.pack()
    window.mainloop()

showwindow()