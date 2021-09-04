# AbBOT

Credit to SeanDaBlack for the basis of the script.

## New Repos

Active development has moved to seperate projects for each effort.

- Python Bot - https://github.com/ramblingjordan/AbBOT-python
- iOS Shortcut - https://github.com/ramblingjordan/AbBOT-iOS-shortcut
- Chrome Extension - https://github.com/ramblingjordan/AbBOT-chrome-extension
- Android App - https://github.com/ramblingjordan/AbBOT-android
- Web Site - https://github.com/ramblingjordan/AbBOT-frontend
- API - https://github.com/ramblingjordan/AbBOT-api

## Discord Server

https://discord.gg/PrAWWCCpDg

### FAQ

If you have a question, before dropping into the Discord, check out our [FAQ page](https://github.com/SeanDaBlack/AbBOT/blob/main/FAQ.md) and see if your question has already been answered.

## Overview

### Files

- `main.py` is the entrypoint for the program.
- `bot/server.py` creates a local web server that serves up a reCaptcha checkbox and passes the reCaptcha token to the `forms.py` file.
- `bot/forms.py` contains the functions used to interact with the forms on the target's website.
- `bot/data.py` contains generators for realistic randomized data.
- `bot/redirection.py` is used to redirect `prolifewhistleblower.com` to `127.0.0.1`
- `bot/static/captcha.html` is our simple reCaptcha checkbox page.
- `bot/logger.py` file for setting up `logging` package.
- `bot/arguments.py` file for getting arguments from the commandline.
- `requirements.txt` contains the required Python3 packages to be installed
- `.style.yapf` is the configuration file for the yapf formatter. Please run `yapf -ri ./bot/` when contributing.
- `FAQ.md` is a list of frequently asked questions and their answers.

## How to use the project

### Clone the repo

```bash
git clone https://github.com/SeanDaBlack/AbBOT.git
cd AbBot
```

### Windows

If you don't already have `python3.exe` and `pip3.exe` installed on Windows, you can install them from the Microsoft Store.


https://www.microsoft.com/en-us/p/python-39/9p7qfqmjrfp7


Now we can install the required Python 3 packages for this project.

```powershell
pip3.exe install -r .\requirements.txt
```

#### Running the program

Please ensure you're running the script with Adminsitrator rights, or someone with read and write access to `C:\Windows\System32\drivers\etc\hosts`.

```
python3.exe .\main.py
```

Then, you will see the following message, "Starting the web server at http://prolifewhistleblower.com:8000/". You will want to open this URL in your browser (works with browsers' Incognito mode if you want to use it). From there you will see a reCaptcha checkbox. Click or solve the reCaptcha and then submit the form.

If you see a message exactly like the following the following in your terminal, then it was successful. If it was not successful, let us know so we can try to fix the issue.

```text
POST request complete.
{"success":true,"data":{"message":"<p>Thank you, we will be working on this shortly.<\/p>","success":true,"behav":"behaviour-hide"}}
```

To exit the program, please hit <kbd>Ctrl</kbd>+<kbd>C</kbd>.

### Linux

If you don't have `python3` or `pip3` installed, you can install the `python3` package with your preferred package manager.

```bash
sudo apt install python3
# or
brew install python3
```

If you already have `python3` installed, make sure your have the latest version of `pip3` installed. You can update your `pip3` installation as follows.

```bash
python3 -m pip install --user --upgrade pip
```

Before you install the required Python 3 packages, you can *optionally* create a virtual environment that will separate the installed packages from your main python installation. A virtual environment creates a local installation of Python, where the installed packages will be isolated from the packages installed by the main Python installation, which allows you to better keep track of what packages are used. This is recommended, especially if you are planning to help develop the bot. The package `venv` is shipped with Python 3.3 or later.

To create a virtual environment, make sure you are in the `AbBOT` directory, then execute:

```bash
python3 -m venv .env
```

This creates a directory `AbBOT/.env`, which contains the virtual Python installation, and will not to uploaded to GitHub during commits. Then source the activate file to use the virtual environment.

```bash
source ./.env/bin/activate
```

To check that you are in virtual environment, the command `which python3` should return a path that ends in `.../AbBOT/.env/bin/python3`. Now you could install the required packages *inside* the virtual environment. To leave the virtual environment and return to your main Python installation, simply use `deactivate`.

Now we can install the required Python 3 packages for this project, regardless of whether or not you are using `venv`.

```bash
python3 -m pip install -r ./requirements.txt
```

#### Running the program

Please ensure you're running the script with sudo, or someone with read and write access to `/etc/hosts`.

```bash
sudo python3 ./main.py
# or
sudo ./main.py
```

If you installed `python3`/`pip3` with `brew` (or installed Python to your account and not to the system in another way), you will want to keep your `PATH` when using `sudo`.

```bash
sudo env "PATH=$PATH" python3 ./main.py
# or
sudo env "PATH=$PATH" ./main.py
```

Then, you will see the following message, "Starting the web server at http://prolifewhistleblower.com:8000/". You will want to open this URL in your browser (works with browsers' Incognito mode if you want to use it). From there you will see a reCaptcha checkbox. Click or solve the reCaptcha and then submit the form.

If you see a message exactly like the following the following in your terminal, then it was successful. If it was not successful, let us know so we can try to fix the issue.

```text
POST request complete.
{"success":true,"data":{"message":"<p>Thank you, we will be working on this shortly.<\/p>","success":true,"behav":"behaviour-hide"}}
```

To exit the program, please hit <kbd>Ctrl</kbd>+<kbd>C</kbd>.

### OSX

If you don't have `python3` or `pip3` installed you can either download the installer from the [Python 3.9.7 release page](https://www.python.org/downloads/release/python-397/) or install it with `brew`.

```bash
brew install python3
```

You could also set up a virtual environment for OS X via `venv` using the same instructions as above in the Linux section.

Now we can install the required Python 3 packages for this project.

```bash
pip3 install -r ./requirements.txt
```


### Generating text dynamically

To make use of a feature that will generate the text of your tip dynamically on each submission, make a free account at [DeepAI](https://deepai.org/machine-learning-model/text-generator) and use the API key generated for you found on your profile page. Set the environment variable 'DEEP_AI_KEY' to this value. This will make it harder to automatically filter out these tips.


#### Running the program

Please ensure you're running the script with sudo, or someone with read and write access to `/etc/hosts`.

```bash
sudo python3 ./main.py
# or
sudo ./main.py
```

If you installed `python3`/`pip3` with `brew` (or installed Python to your account and not to the system in another way), you will want to keep your `PATH` when using `sudo`.

```bash
sudo env "PATH=$PATH" python3 ./main.py
# or
sudo env "PATH=$PATH" ./main.py
```

Then, you will see the following message, "Starting the web server at http://prolifewhistleblower.com:8000/". You will want to open this URL in your browser (works with browsers' Incognito mode if you want to use it). From there you will see a reCaptcha checkbox. Click or solve the reCaptcha and then submit the form.

If you see a message exactly like the following the following in your terminal, then it was successful. If it was not successful, let us know so we can try to fix the issue.

```text
POST request complete.
{"success":true,"data":{"message":"<p>Thank you, we will be working on this shortly.<\/p>","success":true,"behav":"behaviour-hide"}}
```

To exit the program, please hit <kbd>Ctrl</kbd>+<kbd>C</kbd>.

## How it looks in action

![reCaptcha in Chrome on the left side. Terminal running main.py and denoting a successful POST request on the right side.](https://cdn.discordapp.com/attachments/883159187666919549/883350251833028668/unknown.png)

## Usage

```text
usage: main.py [-h] [-v] [-c COUNT]

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Increases the verbosity of the output.
  -c COUNT, --count COUNT
                        Set a maximum number of times to successfully submit to the form.
```
