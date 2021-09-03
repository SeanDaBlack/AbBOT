Wrecksas
--------

This Chromium extension prefills the pro-life whistleblower form with garbage data.  I created this because they added a reCAPTCHA, and this was the easiest way to get around that.  You still have to hit the reCAPTCHA button and submit.  When done, it will refresh, and be filled with new nonsense.

## Installation

* Clone this repo to your machine, or download it as a zip and extract somewhere.
* in Chrome/Chromium, go to `chrome://extensions`
* flip on "Developer mode" in the upper right-hand corner
* click "Load unpacked"
* Browse to this folder.

## Usage

1. Browse to https://prolifewhistleblower.com/anonymous-form/
2. You'll see the form is already filled with arglebargle.
3. Validate that you are not, in fact, a robot
4. Hit submit and wait for the refresh
5. See step 1.

## Modifying

If you add or remove files within `./src`, run `node ./remanifest.js` to make sure `manifest.json` is kept up-to-date, otherwise, you'll get script permission errors.

