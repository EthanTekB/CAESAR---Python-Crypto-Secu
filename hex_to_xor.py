#!/usr/bin/python3
import sys
import os

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

def checkSplitted(splittedString):
    # if (len(splitted) != 2):
    #     print("the provided file must contain only 2 lines")
    #     return False
    if (len(splittedString[0]) != len(splittedString[1])):
        print("the provided 2 strings must have the same length")
        return False
    return True

if (checkSplitted(splitted)):
    hexed = hex(int(splitted[0], 16) ^ int(splitted[1], 16))
    print(hexed[2:].upper())
    exit (0)
else:
    exit (84)
