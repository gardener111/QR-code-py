# required libraries

import getpass
import qrcode
from PIL import Image

# get current users username
username = getpass.getuser()

# use current users username as a string > " + username + "

print ("\nHello, " + username + " and welcome to the QR Code Generator!\n")
print ("You can input your desired URL (website link) to create a QR Code out of it. \nThe script will save it as a image file (.png or .jpg) in a folder.")

# string variable for the URL
url = input("Paste or Enter your URL: ")

# prints out the users input
print (f"This was your URL: \n\n{url}\n")

# let the user specify the name of the image
imgname = input("How would you like to call the generated image?: ")

print (f"Converting to a image with a QR code named:{imgname}...")

# qr code generation module (???)
# img = qrcode.make ({url})
# type(img) # qrcode.image.pil.PilImage
# img.save(f"{imgname}.png")

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(f"{imgname}.png")  

# print successful operaton message
print (f"The QR Code image is stored as '{imgname}.png' in your current working directory.")

