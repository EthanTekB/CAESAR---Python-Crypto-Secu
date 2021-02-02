
#!/usr/bin/python3
import sys

if (len(sys.argv) != 2):
    print("you must provide one parameter")
    exit (84)

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
    try:
        f = open(arg)
        hex = f.read().split('\n')
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
    highest = 0
    key = 0
    for lines in Mybytes:
        M = bytes.fromhex(lines)
        for i in range(256):
            stock = single_char_xor(M, i)
            singlebyte = check_frequency(stock[0])
            if highest == 0 or singlebyte > highest:
                highest = singlebyte
                key = i
    return '{:02x}'.format(key)

def loop_Through2(Mybytes):
    idx = 1
    highest = 0
    key = 0
    for lines in Mybytes:
        M = bytes.fromhex(lines)
        for i in range(256):
            stock = single_char_xor(M, i)
            singlebyte = check_frequency(stock[0])
            if highest == 0 or singlebyte > highest:
                highest = singlebyte
                key = i
                klines = idx
        idx = idx + 1
    return klines


def main():
    mfile = My_OpenFile(sys.argv[1])
    loop = loop_Through(mfile)
    linenum = loop_Through2(mfile)
    print(loop.upper() + " " + str(linenum))

if __name__ == "__main__":
    main()