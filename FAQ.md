# Frequently Asked Questions

## Common issues

1. I'm getting `Form failed to submit.`, what do I do?
   - You can add a `-v` or `--verbose` to the end of your call to `main.py` and it will give you more logs to work with.
2. I'm getting `code 400, message Bad request syntax` and a bunch of garbled text when I click the "Submit" button.
   - This is most likely due to visiting `https://prolifewhistleblower.com:8000/` and not `http://prolifewhistleblower.com:8000/`. The difference here is you need to be on \*\*`http://`. Note: sometimes your browser is sneaky and switches it to `https://` without you knowing.
3. Why can't I go to the actual prolifewhistleblower.com website anymore?
   - You need to <kbd>Ctrl</kbd>+<kbd>C</kbd> out of the script and it will fix your hosts file. In order for the script to work, it redirects that domain back to the script's own web server. If you don't let the script exit normally it won't undo the changes it did to your hosts file.

## Windows issues

1. If you keep getting a message saying that you need to be Adminsistrator yet you are 100% certain that you are Administrator, this is likely a Windows specific issue.
   - Go through this [Windows hosts file troubleshooting guide](https://windowsreport.com/access-denied-hosts-windows-10/) to solve the issue.

## Linux/OSX issues

1. I'm getting `ModuleNotFoundError: No module named 'requests_toolbelt'` even though I've already installed all everything with `pip3 install -r ./requirements.txt`.
   - This likely means that when you're using `sudo` your `PATH` env changes and no longer includes the relevant pip packages that you installed. To fix this, copy over the PATH like it says in the README.
   ```bash
   sudo env "PATH=$PATH" python3 ./main.py
   # or
   sudo env "PATH=$PATH" ./main.py
   ```
   You may also need to run the installation itself as sudo, e.g. `sudo pip3 install -r ./requirements.txt`
