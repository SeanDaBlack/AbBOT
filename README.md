# AbBOT

Credit to SeanDaBlack for the basis of the script.

## Discord Server

https://discord.gg/PrAWWCCpDg

## Overview

### Files

- `server.py` is the entrypoint for the program. It creates a local web server that serves up a reCaptcha checkbox and passes the reCaptcha token to the `forms.py` file.
- `forms.py` contains the functions used to interact with the forms on the target's website.
- `data.py` contains generators for realistic randomized data.
- `redirection.py` is used to redirect `prolifewhistleblower.com` to `127.0.0.1`
- `captcha.html` is our simple reCaptcha checkbox page.
- `requirements.txt` contains the required Python3 packages to be installed
- `.style.yapf` is the configuration file for the yapf formatter. Please run this when contributing.

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
python3.exe .\server.py
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

Now we can install the required Python 3 packages for this project.

```bash
pip3 install -r ./requirements.txt
```

#### Running the program

Please ensure you're running the script with sudo, or someone with read and write access to `/etc/hosts`.

```bash
sudo python3 ./server.py
# or
sudo ./server.py
```

If you installed `python3`/`pip3` with `brew` (or installed Python to your account and not to the system in another way), you will want to keep your `PATH` when using `sudo`.

```bash
sudo env "PATH=$PATH" python3 ./server.py
# or
sudo env "PATH=$PATH" ./server.py
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

Now we can install the required Python 3 packages for this project.

```bash
pip3 install -r ./requirements.txt
```

### Generating text dynamically

To make use of a feature that will generate the text of your tip dynamically on each submission, make a free account at [DeepAI](https://deepai.org/machine-learning-model/text-generator) and use the API key generated for you found on your profile page. Set the environment variable 'DEEP_AI_KEY' to this value. This will make it harder to automatically filter out these tips.

#### Running the program

Please ensure you're running the script with sudo, or someone with read and write access to `/etc/hosts`.

```bash
sudo python3 ./server.py
# or
sudo ./server.py
```

If you installed `python3`/`pip3` with `brew` (or installed Python to your account and not to the system in another way), you will want to keep your `PATH` when using `sudo`.

```bash
sudo env "PATH=$PATH" python3 ./server.py
# or
sudo env "PATH=$PATH" ./server.py
```

Then, you will see the following message, "Starting the web server at http://prolifewhistleblower.com:8000/". You will want to open this URL in your browser (works with browsers' Incognito mode if you want to use it). From there you will see a reCaptcha checkbox. Click or solve the reCaptcha and then submit the form.

If you see a message exactly like the following the following in your terminal, then it was successful. If it was not successful, let us know so we can try to fix the issue.

```text
POST request complete.
{"success":true,"data":{"message":"<p>Thank you, we will be working on this shortly.<\/p>","success":true,"behav":"behaviour-hide"}}
```

To exit the program, please hit <kbd>Ctrl</kbd>+<kbd>C</kbd>.

## How it looks in action

![reCaptcha in Chrome on the left side. Terminal running server.py and denoting a successful POST request on the right side.](https://cdn.discordapp.com/attachments/883159187666919549/883350251833028668/unknown.png)
