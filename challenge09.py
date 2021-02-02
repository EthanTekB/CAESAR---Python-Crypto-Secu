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

def cypherDecode(epitechKey, messageDecoded):
    messageDecoded = pkcs7encode(messageDecoded, len(messageDecoded))
    cipherEncryption = AES.new(epitechKey, AES.MODE_ECB)
    # messageDecoded = pkcs7encode(messageDecoded, 48)
    
    decoded = cipherEncryption.decrypt(messageDecoded)
    decoded = pkcs7decode(decoded, len(messageDecoded))
    # decoded = base64.b64encode(decoded)
    # print(decoded)
    return(decoded)

def hexToBytes(text):
    return (bytes.fromhex(text))

def base64ToBytes(text):
    return (base64.b64decode(text))

def xor(text1, text2):
    return bytes([(a ^ b) for a, b in zip(text1, text2)])

def cipherDecryption(key, iv, dec):
    ivLen = len(iv)
    last_Cipher = bytes.fromhex(iv)
    toReturn = bytes()
    for i in range(0, len(dec) - ivLen, ivLen):
        cipher = dec[i:i + ivLen]
        decriped = cypherDecode(key, cipher)
        # print("&", decriped)
        # print(decriped)
        toReturn += xor(last_Cipher, decriped)
        # print("aaaa", toReturn)
        last_Cipher = cipher
    print(base64.b64encode(toReturn).decode("utf-8"))
    # ase64.b64encode(plaintext).decode('utf-8'))

def main():
    try:
        first_line = hexToBytes(splitted[0])
        second_line = splitted[1]
        third_line = base64ToBytes(splitted[2])
        # print(first_line)
        # print(second_line)
        # print(pkcs7encode(third_line))
        cipherDecryption(first_line, second_line, third_line)
    except:
        print("an error occured")
        exit (84)


if __name__ == "__main__":
    main()