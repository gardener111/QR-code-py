# QR-code-py - Open Source QR Code Generator

version 1.1

a small project of coding a QR code generator mainly for personal uses.

*scroll down for the tutorial if you already know how to use python scripts in your terminal*

If you got frustrated trying to create/generate a QR code for free on the internet and have been annoyed with login prompts or paywalls, and somehow ended up here... im glad!

No matter what you do, a self generated QR code can come in handy. Especially if its not time-sensitive or doesn't require you to set up and accepts T&C's. By cloning this repo (or simply downloaded a nicely packed .exe in a .zip in the future...) you will be able to do that!


## Goals

The goals for this project actually split into two sections.
The first section is of course, what i want to give to you, the users, and the other is a personal goal i want to achieve by making this project.

- What i want to give you all?
	- as previously stated, a free and open source QR Code generator
	- for CLI enthusiasts, this tool but in a CLI format!
	- for anyone else, either a .exe program to just run and generate a QR Code.


## Documentation

While doing this project and by learning git, and markdown files, i will split the full documentation into separate chunks with code snippets, screenshots, references and sources, which is available for any one who might be interested in the projects directory "Notes" or "Screenshots"

# Tutorial

To run this script on your local machine after cloning this repo, you need to make a few steps in your terminal (aside the 'program' itself running in the terminal). You can follow this tutorial to do this!

### Linux or macOS

*Open your terminal and run:*
```bash
git clone https://github.com/gardener111/QR-code-py.git
```

*then navigate to the cloned repo:*
```bash
cd QR-code-py
```

*create a virtual environment*
```bash
python3 -m venv .venv
```

*activate the virtual environment*
```bash
source .venv/bin/activate
```

*install dependencies*
```bash
pip install -r requirements.txt
```

*run the script*
```bash
python3 main.py
```

### Windows(CMD/Powershell)

The process is pretty much the same, once you open your Windows Terminal/cmd/Powershell you will be in the 'home' directory by default, unless you specified it to launch differently. You can simply just do '*git clone*' as stated below or navigate to your Desktop directory so you can see what you clone and where it is easily. You can do so by running:

**optional** *Move directory*
```powershell
cd '.\Desktop\'
```

and proceed with the command below. Otherwise if you know how to navigate files in command line, you may proceed with the command below without changing directories...

*open your Windows Terminal and run:*
```powershell
git clone https://github.com/gardener111/QR-code-py.git
```
```

*create the virtual environment*
```powershell
python3 -m venv .venv
```

*activate the virtual environment (if using CMD)*
```powershell
.venv\Scripts\activate.bat
```

*activate the virtual environment or (if you are using PowerShell)*
```powershell
.venv\Scripts\Activate.ps1
```

*install dependencies*
```bash
pip install -r requirements.txt
```

*run the script*
```bash
python3 main.py
```

*To **deactivate** the virtual environment run this command (works on all OS's):*

```bash
deactivate
```

I hope you have made use of my code! Feel free to clone it and customize it how ever you want!

Test the QR Code results!

![qr-code](https://github.com/gardener111/QR-code-py/blob/main/see-if-it-works.png "Scan me to see if it works!")