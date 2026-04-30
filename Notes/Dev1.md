# Notes from the newest development

In the current branch 'directory_choice' i made a new library implementation.

First new library used is 'platform'. This let me print out the OS the script is running on.

```python
import platform
os = platform.system()
print (f"You are running this script on {os}.\n")
```

the 'print' statement prints out the OS the user is running the script on like: Windows, Linux, macOS.

Next i wanted to give the user a choice to choose the directory to save the generated QR Code. For that i used the library called 'pathlib'. After defining users home directory, the most user friendly option i went with was with a choice of numbers from 1 to 4. Number 1 being the current working directory (**cwd**) and number 4 being the Downloads directory, as seen below.

```python
import pathlib
# get the users Home directory (unified over all OS's)
home_dir = pathlib.Path.home()
# define common directories for different OS's
dir = {
    "1": pathlib.Path.cwd(),
    "2": home_dir / "Desktop",
    "3": home_dir / "Documents",
    "4": home_dir / "Downloads"
}
```

Using a dictionary data structure i created the key-value pairs defining the directory choice. Each choice being a string ("1", "2", "3" ...) and each value being a **pathlib.Path** object. After the first option returning users current working directory the next options use pathlib's "/" operator to join the users home directory with a subfolder name, which figures out the OS and the directory path structure saving the energy and time for typing C:\Users\\{username}\Desktop or /home/{username}/desktop.

Another dictionary i needed to use was, directory labels. The key-values here were of course labling the choices that were to be made by the user. These key-values were separating the values from the dictionary structure shown earlier ('dir'). I needed to implement the separation because i wanted to print out a confirmation which is easy to understand for a not-so-tech-savvy end user.

```python
dir_labels = {
    "1": "current working directory",
    "2": "Desktop",
    "3": "Documents",
    "4": "Downloads"
}
```

An important thing in the whole idea of giving the user a choice was to specify which choices the user will have and implement it as a if/else statement in the code. A recently learned was that a if/else statement doesnt need to have a long chain. By practically saying 'if the directory choice ('dir_choice' as inputted number) is in the directory table (that i specified in 'dir') then print "xyz string". You see, instead of...

```python
if dir_choice == "1" or dir_choice == "2" or dir_choice == "3" ...
```

... i decided to just do ...

```python
if dir_choice in dir:
    save_dir = dir[dir_choice]
    print(f"You have chosen to save the image in {dir[dir_choice]}.\n")
else:    
    save_dir = pathlib.Path.cwd()
    print("Invalid choice. The image will be saved in the current working directory by default.\n")
```

But another new thing i added here to fulfill the goal is 'save_dir'. This variable assigns a value which was earlier specified by the user, which is in the 'dir' table and is inputted by the user with a number in 'dir_choice', informing the user. If the user chooses none of the numbers like: "2" for Desktop or "3" for Downloads, then it just sets the value of the 'save_dir' variable to be the current working directory, informing the user about their choice.

A quick necessary checkpoint in the project is where the script checks the specified directories availability, and if it doesn't exist, it will create it.

```python
 # check if directory already exists and if not, create it
pathlib.Path(save_dir).mkdir(parents=True, exist_ok=True)
```

There have also been some changes for the module generating the QR Code. I basically just used the code from the libraries official [website](https://pypi.org/project/qrcode/)that adds more control over how the QR Code is generated. 

```python
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)
```

I mainly opted to have the version variable set to 'None' because it automatically sets the size of the QR Code based on the inputted URL as well as having the qr.make module fit automatically.

Completing the task of saving the file to a user-specified directorywas just to create another variable called 'save_path' and telling the code to save the image in the actual path that it was told to.

```python
img = qr.make_image(fill_color="black", back_color="white")
save_path = save_dir / f"{imgname}.png"

img.save(save_path)
```

I could not resist and needed to put a information for the user in case of any confusion, just to make things clear haha.

```python
print (f"The QR Code image is stored as '{imgname}.png' in:\n\n {save_dir}\n")
```