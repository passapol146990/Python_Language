import qrcode

def generate_qr_code(title, data):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f'{title}.png')

title = input('Enter the title of your QR code: ')
data = input('Enter the data you want to encode in the QR code: ')
generate_qr_code(title, data)
