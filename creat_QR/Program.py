from tkinter import*
from tkinter import ttk
import qrcode
from PIL import ImageTk
import pyautogui as at

def create_qrcode(text):
    qr = qrcode.QRCode()
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    return img

def win2():
    def on_click():
        txt = inputtext.get('0.0','end-1c')
        img = create_qrcode(txt).resize((250,250))
        img1 = ImageTk.PhotoImage(img)
        QR.configure(image=img1)
        QR.image = img1



    def save_qr():
        name = str(at.prompt(title='ตั้งชื่อรูป',text='ใส่ชื่อรูป')) + '.png'
        txt = inputtext.get('0.0','end-1c')
        if name == 'None.png':
            pass
        else:
            create_qrcode(txt).save(name)
            create_qrcode(txt).show()

    win = Tk()
    win.minsize(height=560,width=800)
    win.title('สร้างคิวอาร์โค้ด')

    Label().pack()

    text1 = ttk.Label(text='ใส่ ลิ้งก์/URL หรือใส่ตัวหนังสือที่ต้องการ',font=('angsana New',40))
    text1.pack()

    Label().pack()

    inputtext = Text(height=4,width=80,fg='black',background='white')
    inputtext.pack()

    Label().pack()

    ok =ttk.Button(win,text='OK',command=on_click)
    ok.pack(ipadx=20,ipady=5)

    Label().pack()

    QR = Label(win)
    QR.pack()

    Label().pack()

    save = ttk.Button(win,text='Save',command=save_qr)
    save.pack(ipadx=20,ipady=5)

    Label().pack()


    win.mainloop()
win2()