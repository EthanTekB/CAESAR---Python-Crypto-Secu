#!/usr/bin/python3
import sys
import codecs
import os
import string
import binascii

letter_value = {
' ' : 700000000,
'e' : 390395169,
't' : 282039486,
'a' : 248362256,
'o' : 235661502,
'i' : 214822972,
'n' : 214319386,
's' : 196844692,
'h' : 193607737,
'r' : 184990759,
'd' : 134044565,
'l' : 125951672,
'u' : 88219598,
'c' : 79962026,
'm' : 79502870,
'f' : 72967175,
'w' : 69069021,
'g' : 61549736,
'y' : 59010696,
'p' : 55746578,
'b' : 47673928,
'v' : 30476191,
'k' : 22969448,
'x' : 5574077,
'j' : 4507165,
'q' : 3649838,
'z' : 2456495,
}


def check_frequency(Mybytes):
    score = 0
    for i in Mybytes:
        score += letter_value.get(chr(i), 0)
    return score

def My_OpenFile(arg):
    myPath = os.getcwd() + "/" + arg
    try:
        f = open(myPath)
        hex = f.read()
        return (hex)
    except:
        print('an error has occured: File is invalid or does not exist')
        exit(84)

def single_char_xor(ib, cv):
    ob = b''
    for byte in ib:
        ob += bytes([byte ^ cv])
    return ob, cv

def loop_Through(Mybytes):
    Mybytes = bytes.fromhex(Mybytes)
    key = 0
    highest = 0
    for i in range(256):
        stock = single_char_xor(Mybytes, i)
        singlebyte = check_frequency(stock[0])
        if highest == 0 or singlebyte > highest:
            highest = singlebyte
            key = i
    return '{:02x}'.format(key)

def main():
    file = My_OpenFile(sys.argv[1]).lower()
    loop = loop_Through(file)
    print(loop)

if __name__ == "__main__":
    main()
    