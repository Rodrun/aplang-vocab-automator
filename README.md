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
