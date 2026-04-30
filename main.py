# required libraries
import getpass
import qrcode
from PIL import Image
import platform
import pathlib

# get current operating system
os = platform.system()

# get current users username
username = getpass.getuser()

# use current users username as a string > " + username + "

print ("\nHello, " + username + " and welcome to the QR Code Generator!\n")
print (f"You are running this script on {os}.\n")
print ("First you will need to specify the directory you would like to save the generated QR Code image in.\n")

# get the users Home directory (unified over all OS's)
home_dir = pathlib.Path.home()

# define common directories for different OS's
dir = {
    "1": pathlib.Path.cwd(),
    "2": home_dir / "Desktop",
    "3": home_dir / "Documents",
    "4": home_dir / "Downloads"
}

# label specific directory choices for user input
dir_labels = {
    "1": "current working directory",
    "2": "Desktop",
    "3": "Documents",
    "4": "Downloads"
}

# directory choice input
dir_choice = input(
    "To simplify the process, choose a number from 1 to 4 to select the directory you want to save the image in:\n\n"
    "1. Current working directory (default)\n"
    "2. Desktop\n"
    "3. Documents\n"
    "4. Downloads\n"
)

# confirm directory choice in path
if dir_choice in dir:
    save_dir = dir[dir_choice]
    print(f"You have chosen to save the image in {dir[dir_choice]}.\n")
else:    
    save_dir = pathlib.Path.cwd()
    print("Invalid choice. The image will be saved in the current working directory by default.\n")

 # check if directory already exists and if not, create it
pathlib.Path(save_dir).mkdir(parents=True, exist_ok=True)
print (f"Input your desired URL (website link) to create a QR Code out of it. \nThe script will save it as a image file (.png or .jpg) in {save_dir}.\n")

# input string variable for the URL
url = input("Paste or Enter your URL: ")

# prints out the users input
print (f"This was your URL: \n\n{url}\n")

# let the user specify the name of the image
imgname = input("How would you like to call the generated image?: ")
print (f"Converting to a image with a QR code named:{imgname}...")

# qr code generation module
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# save the QR code image to the specified directory
img = qr.make_image(fill_color="black", back_color="white")
save_path = save_dir / f"{imgname}.png"

img.save(save_path)  

# print successful operaton message
print (f"The QR Code image is stored as '{imgname}.png' in:\n\n {save_dir}\n")

