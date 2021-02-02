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

def pkcs7decode(bytestring, k=16):
    val = bytestring[-1]
    # if val > k:
    #     raise ValueError('Input is not padded or padding is corrupt')
    l = len(bytestring) - val
    return bytestring[:l]

def pkcs7encode(bytestring, k=16):
    l = len(bytestring)
    val = k - (l % k)
    return bytestring + bytearray([val] * val)

def main():
    try:
        epitechKey = bytearray.fromhex(splitted[0]).decode()
        cipherEncryption = AES.new(epitechKey, AES.MODE_ECB)
        allText = "".join(splitted[1:])
        messageDecoded = base64.b64decode(allText)
        # messageDecoded = pkcs7encode(messageDecoded, 48)
        
        decoded = cipherEncryption.decrypt(messageDecoded)
        decoded = pkcs7decode(decoded)
        decoded = base64.b64encode(decoded)
        print(decoded.decode("ascii"))
    except:
        print("an error occured")
        exit (84)


if __name__ == "__main__":
    main()
    