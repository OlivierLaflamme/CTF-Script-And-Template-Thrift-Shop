import binascii

def XORBreak(h):
    en = binascii.unhexlify(h)
    for key in range(256):
        de = ''.join(chr(b ^ key) for b in en)
        if de.isprintable():
            print(de + "\n")

with open("text.txt") as f:
    for line in f:
        XORBreak(line.strip())
