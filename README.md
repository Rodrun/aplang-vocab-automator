# aplang-vocab-automator
AP Lang vocab list definition finder. Enter your vocab list without definitions, and I'll find your 1st merriam-webster definition of each.

## Dependencies

Can be installed with `pip`.

- [requests](https://pypi.python.org/pypi/requests/2.18.4)
- [beautifulsoup4](https://pypi.python.org/pypi/beautifulsoup4)

## How to run

First of all, clone to a directory and navigate to it. For example `git clone https://github.com/rodrun/aplang-vocab-automator ; cd aplang-vocab-automator`

1. Create a virtual python environment in the local directory
```
$ python3 -m venv avenv .
```
2. Activate the virtual environment
- \*Nix/OSX (bash/zsh)
```
$ source avenv/activate
```
- Windows (cmd.exe)
```
C:\> avenv/Scripts/activate.bat
```
3. Install the dependencies
```
$ pip install requests beautifulsoup4
```
4. Run
```
$ python3 vocab-formatter.py
```

## Limitations

Each vocabulary word must be in a new line. If a vocab word has a colon (:) after it, it is fine, because I made it specifically for a vocab list that my English teacher gives out, and it includes a colon after each words with other letters like "n., adj., etc..." So if you have something like `amorpheous: n.`, the script will only look for the token before the colon.

*Note:* I do **not** *think* that words with spaces will work correctly, however, I have not tested this *yet*. This includes something like `geology ` or ` geology`, etc. with whitespace leading or trailing.
