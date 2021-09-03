# AbBOT

Credit to SeanDaBlack for the basis of the script.

## Overview

### Files

- `server.py` is the entrypoint for the program. It creates a local web server that serves up a reCaptcha checkbox and passes the reCaptcha token to the `forms.py` file.
- `forms.py` contains the functions used to interact with the forms on the target's website.
- `data.py` contains generators for realistic randomized data.
- `redirection.py` is used to redirect `prolifewhistleblower.com` to `127.0.0.1`
- `captcha.html` is our simple reCaptcha checkbox page.
- `requirements.txt` contains the required Python3 packages to be installed
- `.style.yapf` is the configuration file for the yapf formatter. Please run this when contributing.

## Setup

### Clone the repo

```bash
git clone https://github.com/SeanDaBlack/AbBOT.git
cd AbBot
```

### Windows

If you don't already have `python3.exe` and `pip3.exe` installed on Windows, you can install them from the Microsoft Store.

https://www.microsoft.com/store/productId/9P7QFQMJRFP7

Now we can install the required Python 3 packages for this project.

```bash
pip3.exe install -r requirements.txt
```

### Linux

If you don't have `python3` or `pip3` installed, you can install the `python3` package with your preferred package manager.

#### `apt`

```bash
sudo apt install python3
```

Now we can install the required Python 3 packages for this project.

```bash
pip3 install -r requirements.txt
```

### OSX

You will probably need to go get the chrome driver to make selenium work, as they are version-specific. The one in the repo might not do it for you. Find your chrome version by going to **Chrome** >> **About Google Chrome**.

This will open a tab that shows you your verison. Visit https://sites.google.com/chromium.org/driver/downloads and download the driver for your version.

folder. Extract the downloaded zip file. Move the extracted chromedriver binary to this project folder

`mv ~/Downloads/chromedriver .`

It needs to be found in your `PATH` variable.

`export PATH=$PATH:$(pwd)`

You might also get a trust issue with the downloaded driver being unverified. To fix that, run

`xattr -d com.apple.quarantine chromedriver`

this just tells the OS it's safe to use this driver, and Selenium will start working. See https://timonweb.com/misc/fixing-error-chromedriver-cannot-be-opened-because-the-developer-cannot-be-verified-unable-to-launch-the-chrome-browser-on-mac-os/ for more info.

`python req.py` to run. It will loop until you kill the job. `ctrl + c` in your terminal to give the pro lifes a break (optional).
