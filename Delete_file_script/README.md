# [Delete file-Python script](https://github.com/sthsuyash/Delete-file-Script/blob/main/deleteScript.py)
## For Windows

Executable app '.exe' is inside [dist](https://github.com/sthsuyash/Delete-file-Script/tree/main/dist) directory

Simple python script to delete:

- all files with given extension.
- files with given names.
- given folder

The program:

- takes extension input from the user.
- requires operating system module to access the current directory and delete access
- traverses through all the files in folder to check the condition and removes if found.

```
Used pyinstaller to create .exe file
```
<br/><br/>

- Add python to Path
- Install the Pyinstaller package

```terminal
pip install pyinstaller
```

- Save your python script

```python
pyinstaller --onefile script.py
```

- Run the executable
