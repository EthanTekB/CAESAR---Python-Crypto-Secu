#!/usr/bin/python3
import sys
import base64

if (len(sys.argv) != 2):
    print("you must provide one parameter")
    exit (84)

def challenge01(arg):
    try:
        f = open(arg)
        hex = f.read()
    except:
        print('an error has occured: File is invalid or does not exist')
        exit(84)
    if hex == "":
        print('an error has occured: file is empty')
        exit(84)
    try:
        tmp = bytes.fromhex(hex)
        enc = base64.b64encode(tmp)
    except:
        print('an error has occured: string is not Hexadecimal')
        exit(84)
    tmp1 = enc.decode()
    print(tmp1)

    
challenge01(sys.argv[1])