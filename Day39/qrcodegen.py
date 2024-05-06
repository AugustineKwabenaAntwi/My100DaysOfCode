import qrcode
import qrcode.constants

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size =10,
        border = 4,
    )

    qr.add_data(text)

    qr.make(fit=True)
    img = qr.make_image(fill_color = 'green', back_color='white')
    img.save("qrimg.png")

url=input("Enter your URL: ")
generate_qrcode(url)