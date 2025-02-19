#install qrcode so that you can import it
#Open the terminal or command prompt and run:  pip install qrcode for simple usage OR
#FOR more customized usage: install pip install "qrcode[pil]"


#objective is to make a QR Coded, when scanned, will take us my github page beginner friendly page.

import qrcode

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 10,
    border = 4,
)
#Error Correction: ERROR_CORRECT_L = About 7% or less errors can be corrected. ERROR_CORRECT_M (default) = About 15% or less errors can be corrected. ERROR_CORRECT_Q = About 25% or less errors can be corrected. ERROR_CORRECT_H. About 30% or less errors can be corrected.
#use the qr code to get us to my github repository.
qr.add_data("https://github.com/PakouLee/Python-Projects-Beginner-Friendly")
qr.make(fit = True)  #Usually a default, so you may not need to specify it here.

#here we can specify more parameters if needed.
img = qr.make_image(fill_color = "black", back_color = "white")

#save the QR code image. Don't forget to state the image type. for instance is it png or jpeg.
img.save ("Beginner_Friendly_Projects.png")

