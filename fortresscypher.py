import binascii
def makeList(stringVal): 
    list = []
    for c in stringVal: 
        list.append(c) 
    return list

def superCrypt(stringVal, keyVal): 
    keyPos = 0 
    key = makeList(keyVal) 
    xored = []
    for c in stringVal: 
        xored.append(binascii.hexlify(chr(ord(c) ^ ord(keyVal[keyPos])))) 
        if keyPos == len(key) - 1: 
            keyPos = 0
        else:
            keyPos += 1 
    hexVal = ''
    for n in xored: 
        hexVal += n
    return hexVal

with open('message.txt') as f: 
    content = f.read()

key = sys.argv[1]

with open('encrypted.txt', 'w') as f: 
    output = f.write(binascii.unhexlify(superCrypt(content, key)))
