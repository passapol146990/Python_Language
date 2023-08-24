from tkinter import*
from PIL import Image,ImageTk
import qrcode
import pyautogui as at
def create_qrcode(text):
    qr = qrcode.QRCode()
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black',back_color='white')
    return img


url = at.prompt(text='URL to a QR code',title='Enter URL')
if url == None:
    pass
else:
    create_qrcode(url).show()
