# Overall Project Notes

After multiple additions and restructurizing of the repo, aswell as creating a basic python script doing any action (only printing now) i decided to start creating notes, for future reference and to document what i have learned so far.

_if you have any syntax correction advices, please share!_

### First actions

So i decided to create a "main.py" where the main, stable build of the project will be living. To make the script do something, just a simple task i wanted to print a simple line and pull the current users username from the system so that the program will have a nice "greeting".

```python
import getpass

# get current users username
username = getpass.getuser()

print ("this will be a QR code generator")
print ("Hello, " + username + "")
```

Which looks like this:

![alt text](https://github.com/gardener111/QR-code-py/blob/main/Screenshots/demo_script_output.png)

As i have only pulled the current users username previously only on PowerShell, i needed to google how to do that in python! I found some helpful information [here](https://stackoverflow.com/questions/842059/is-there-a-portable-way-to-get-the-current-username-in-python).

I forgot to create a virtual environment for the project which also needs to be pushed into the repo, so I did that too.

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

As i already have a python virtual environment running to test the script, i needed to install libraries required for this project.

```bash
pip install qrcode[pil]
```

```bash
pip list
```

Reference Screenshot:

![alt text](https://github.com/gardener111/QR-code-py/blob/main/Screenshots/venv%2Bpip_packages.png)

## Coding the main script

After creating a 'main.py' script as a demo code that runs pretty much any command (very simple strings and usernames etc.) it was time to make it work as intended. Very simple, no GUI, just a CLI so it gets the job done.

I had to greet the user properly and tell them what and how will be done. In simple terms.

```python
# get current users username
username = getpass.getuser()

# use current users username as a string > " + username + "

print ("\nHello, " + username + " and welcome to the QR Code Generator!\n")
print ("You can input your desired URL (website link) to create a QR Code out of it. \nThe script will save it as a image file (.png or .jpg) in a folder.")

# string variable for the URL
url = input("Paste or Enter your URL: ")
```
As you can see i decided to include a prompt for the user at the beginning so they can move through with the generation as fast as possible. 

This gave us this output:

![alt text](https://github.com/gardener111/QR-code-py/blob/main/Screenshots/start-prompt.png)

For transparency with users input, i decided to print out users URL so they could double check.
I also wanted to provide a customization option, so i added a string variable where the user could call the file thats to be generated as they want.

```python
# let the user specify the name of the image
imgname = input("How would you like to call the generated image?: ")
```

And to conclude, and complete the main functionality of this script i simply used the official qrcode library documentation on pythons website, which can be found [here](https://pypi.org/project/qrcode/).

```python
# qr code generation module (???)
img = qrcode.make ({url})
type(img) # qrcode.image.pil.PilImage
img.save(f"{imgname}.png")

# print successful operaton message
print (f"The QR Code image is stored as '{imgname}.png' in your current working directory.")
```

Another addition seen in the code snapshot above, is just my need to communicate with the user. I think this gives a simple CLI Script a feel of a GUI Demo where the dev displays basic informational messages to the end user.

_this may even be bare minimum but im not a dev so how would i know..._ 

The end "product" looks like this:

![alt text](https://github.com/gardener111/QR-code-py/blob/main/Screenshots/final-main.png)

### To Do

By default the script saves the file in the repo directory. In my opinion, my thoughts behind it were that i want the user to specify the directory to save the QR Code image.
Whats may also be important is the size of the QR Code that will be generated. There is a qrcode variable to be set to determine this automatically which, in my understanding picks the size automatically.

**done \\/**

*testing*