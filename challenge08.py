#!/usr/bin/python3
from Crypto.Cipher import AES
import sys
import base64

if (len(sys.argv) != 2):
    print("you must provide one parameter")
    exit (84)

def readFile(arg):
    try:
        f = open(arg)
        rea = f.read()
        f.close()
        return (rea)
    except IOError:
        print("could not find " + sys.argv[1])
        exit(84)

readed = readFile(sys.argv[1])
splitted = readed.split("\n")

def countNumberOfOccurences():
    rep = []
    for i in range(0, len(splitted), 1):
        splitted[i] = base64.b64decode(splitted[i])
        tmp = []
        for index in range(0, len(splitted[i]), 8):
            tmp.append(splitted[i][index:index + 8])
        rep.append((len(tmp) - len(set(tmp)), i))
    
    print(max(rep)[1] + 1)

def main():
    try:
        countNumberOfOccurences()
    except:
        print("an error occured")
        exit (84)


if __name__ == "__main__":
    main()