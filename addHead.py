#!/usr/bin/python3

import sys
from pathlib import Path


def getContentOriginalFile(_file):
    file = open(str(_file), 'r+')
    content = file.read()
    file.close()
    return content

def checkHeaderIsPresent(_file, header):
    file = open(str(_file), 'r+')
    content = file.read()
    file.close()
    return header in content


originHeader = "$START >> HEADER HERE << $END\n\n\n"


headerTest = 'Check header if present'

commentSymbole = {'start': '', 'end': ''}

if (len(sys.argv) > 1):
    extension = sys.argv[1].lower()
    if (extension == "html"):
        commentSymbole['start'] = '<!--'
        commentSymbole['end'] = '-->'
    else:
        commentSymbole['start'] = '/*'
        commentSymbole['end'] = '*/'
        
    header = originHeader.replace("$START",commentSymbole['start']).replace("$END",commentSymbole['end'])

    for filename in Path('.').glob('**/*.' + extension):
        try:
            if (checkHeaderIsPresent(filename, headerTest) == False):
                originalContent = getContentOriginalFile(filename)
                with open (str(filename), 'w+') as file:
                    file.write(header + originalContent)
                    print(str(filename) + ' -> Traité')
            else:
                print(str(filename) + ' -> Header already exist')
        except:
            pass
                
else:
    raise ValueError


