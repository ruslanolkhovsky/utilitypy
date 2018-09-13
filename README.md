# utilitypy
A package of miscellaneous python utilities and programs


## file_str_replace.py

A simple utility program in python 3 to replace a string (--find or -f) all over a file (--sourcefile or -s) with a new string (--replace or -r) and save the result to a new file (--target or -t, optional).

Examples:
```
$ python3 file_str_replace.py --sourcefile 'file.txt' --find 'A' --replace 'B' --target 'new_file.txt'
```
```
$ python3 file_str_replace.py -s 'file.txt' -f 'A' -r 'B'
```
