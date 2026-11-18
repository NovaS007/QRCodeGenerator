import qrcode
from qrcode.constants import ERROR_CORRECT_H

if __name__ == "__main__":
    pdf_url = input("Enter the URL of the PDF file: ")
    color = input("Please enter the hex code of the color you want for the QR code (e.g., #BF504D): ")
    path_to_save = input("Enter the path where you want to save the QR code image (e.g., /Users/username/Desktop/qr_code.png): ")

    qr = qrcode.QRCode(
        version=2,
        error_correction=ERROR_CORRECT_H,
        box_size=12,
        border=4,
    )

    qr.add_data(pdf_url)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color=color
    )

    img.save(path_to_save)