"""A simple utility program in python 3 to replace a string all over a file with a new string, and save the result to a new file.

Example:
``
$ python3 file_str_replace.py -s 'file.txt' -f 'A' -r 'B' -t 'new_file.txt'
``

Arguments:

--sourcefile, -s    Name of the source file (required)

--find, -f          String to be find and replaced with the new one (required)

--replace, -r       The new string to replace the existing string (required)

--target, -t        Name of the target file (optional). If not defined,
                    the program creates a new file with the extension .new
                    in the same location.
"""

import sys
from argparse import ArgumentParser, FileType

def CreateParser ():

    parser = ArgumentParser()

    parser.add_argument ('--sourcefile', '-s ', type=FileType('r', encoding='UTF-8'), required=True, help='Name of the source file (required)')
    parser.add_argument ('--find', '-f ', type=str, required=True, help='String to be find and replaced with the new one (required)')
    parser.add_argument ('--replace', '-r ', type=str, required=True, help='The new string to replace the exsisting string (required)')
    parser.add_argument ('--target', '-t ', type=FileType('w'), required=False, help='Name of the target file (optional). If not defined, the program creates a new file with the extension .new in the same location.')

    return parser

if __name__ == "__main__":
    # Parsing arguments
    parser = CreateParser()
    params = parser.parse_args(sys.argv[1:])

    # Reading the source file to the list
    with params.sourcefile as file:
        text = [line.rstrip('\n') for line in params.sourcefile]
        file.close()

    # Checking if the name of the target file is defined in the arguments
    # and set the name by deafault if not
    if not params.target:
        targetfile = open(params.sourcefile.name + ".new", "wt")
    else:
        targetfile = params.target

    # Replacing the string and writing the output to the target file
    with targetfile:
        for line in text:
            if params.find in line:
                targetfile.write(line.replace(str(params.find), str(params.replace)) + '\n')
            else:
                targetfile.write(line + '\n')

    print("Done. Target file: " + targetfile.name)
    targetfile.close()
