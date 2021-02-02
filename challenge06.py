#!/usr/bin/python3
import sys
import codecs
import os
import string
import binascii

def calculate_BytArray(arrbytes):
    myArr = []
    for byt in arrbytes:
        myArr.append(byt)
    return(myArr)

def hammdist(string1, string2):
    dist = 0
    array1 = bytes(string1, 'ascii')
    array2 = bytes(string2, 'ascii')
    bytArray1 = calculate_BytArray(array1)
    bytArray2 = calculate_BytArray(array2)
    XordArr = []
    for byt1, byt2 in zip(bytArray1, bytArray2):
        XordArr.append(byt1 ^ byt2)
    for xorbyte in XordArr:
        for bits in bin(xorbyte):
            if (bits == '1'):
                dist += 1
    return dist 

print(hammdist('Hello', 'World'))