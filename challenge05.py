#!/usr/bin/python3
import sys

def My_ReadFlineFile(arg):
    try:
        f = open(arg)
        fline = f.readline().strip()
        return (fline)
    except:
        print('an error has occured: File is invalid or does not exist')
        exit(84)


def My_OpenFile(arg):
    try:
        f = open(arg)
        next(f)
        hex = f.read().replace('\n', '')
        return (hex)
    except:
        print('an error has occured: File is invalid or does not exist')
        exit(84)

def repeating_xor(hext, hkey):
    Encbytes = b''
    i = 0
    tmp = ""
    for bytenum in hext:
        Encbytes = Encbytes + bytes([bytenum ^ hkey[i]])
        if (i + 1) != len(hkey):
            i = i + 1
        else:
            i = 0
    return (Encbytes.hex().upper())

def main():
    if (len(sys.argv) == 2) :
        myKey = bytes.fromhex(My_ReadFlineFile(sys.argv[1]))  #.lower()
        mfile = bytes.fromhex(My_OpenFile(sys.argv[1]))
        #print(mfile)
        result = repeating_xor(mfile, myKey)
        print(result)
    else:
        print('ERROR: there is too many or not enough arguments')
        exit(84)



if __name__ == "__main__":
    main()
    