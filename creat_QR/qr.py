from tkinter import*
import qrcode
from PIL import Image,ImageTk

def create_qrcode(text):
    qr = qrcode.QRCode()
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    return img

def window():
    def on_click(e):
        input_text = txt.get('0.0','end-1c') # 0.0 เอามาตัวแรกจนตัวสุดท้าย end-1c ไม่ต้องเอาเว้นวรรค
        img = create_qrcode(input_text).resize((250,250))
        imgTk = ImageTk.PhotoImage(img)
        qr.configure(image=imgTk)
        qr.image = imgTk
        
    win = Tk()
    win.minsize(height=400)
    win.title('Phol Create QR code')
    # win.option_add('*Font','consolas 20')
    Label(win, font=20 ,text='input text To create a QR Code').grid(row=0,column=0)
    txt = Text(win,height=4,width=30,fg='black')
    txt.grid(row=1,column=0)
    btn = Button(win,text='Create QR Code',bg='gold',fg='black',font=20)
    btn.grid(row=2,column=0)
    btn.bind('<Button-1>',on_click)
    qr= Label(win)
    qr.grid(row=3,column=0,rowspan=1)


    win.mainloop()
window()


# create a QR Code object 