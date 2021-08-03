import sys
import string

def d2b(char):
    return bin(char)[2:].rjust(7,'0')
    return bin(char)[2:].rjust(7,'0')

def numberTruncate(number, precision, scale):
    '''
    DescriptionTruncates a number.
    number: The number to truncate, starting with the leftmost.
    precision: The number of digits to display, starting with the leftmost.
    scale: The number of digits to the right of the decimal point. 
    The precision parameter must be large enough to hold the number of digits that you specify in this parameter.
    '''
    return int(number)
#    return int(round(number, 0))
#    return int(str(int(round(number, 0)))[:2])

def strMidX(string, start, length):
    return string[start:start+length]

def encrypt(clearPassword):
    binaryNumber = ''
    preSwapBinaryText = ''
    encryptPassword = ''
    charASCIINum = 0
    length = 0
    origLength = 0
    index = 0
    swapPosition = 0
    position = 0
    
    length = len(clearPassword)
    origlength = length
    
    #loop string to bin
    while index < length:
        charAsciiNum = ord(clearPassword[0])
        clearPassword = clearPassword[1:]
        binaryNumber = d2b(charAsciiNum)
        preSwapBinaryText += binaryNumber
        index += 1
    
    #padding
    length = len(preSwapBinaryText)
    while len(preSwapBinaryText) < 70:
#        binaryNumber = d2b(90 + numberTruncate(len(preSwapBinaryText)/2, 2, 0))
        binaryNumber = d2b(90 + numberTruncate(len(preSwapBinaryText)/2, 2, 0))
#        print(90 + numberTruncate(len(preSwapBinaryText)/2, 2, 0))
        preSwapBinaryText += binaryNumber
    
    swapPosition = 2 + int(strMidX(preSwapBinaryText, 5, 1))
    length = len(preSwapBinaryText)
    index = 0
    
    while True:
        encryptPassword += strMidX(preSwapBinaryText, position, swapPosition - 1)
        position += swapPosition - 1
        encryptPassword += strMidX(preSwapBinaryText, position + 1, 1)
        encryptPassword += strMidX(preSwapBinaryText, position, 1)
        position += 2
        if position >= length: break
        
    return encryptPassword
    
dic = string.printable
#print(dic)
flag1 = ''
flag = 'FLAG'
encflag = open('crapto_century.cipher','r').read()

#print(encflag[:5*7])
#enc = encrypt(flag)
#print(enc)

#print(enc[:len(flag)*7])
#print(encflag[:len(flag)*7])

#print()

#print(encrypt(flag))


while True:
    s = len(flag)
    
    pot = []
    for char in dic:
#    for i in range(0xff):
#        char = chr(i)
        temp = flag + char
        enc = encrypt(temp)
    #    print(char,temp,enc)
        toComp = enc[:len(temp)*7]
        
        print(char, encflag[-7:], toComp[-7:])
        if encflag[:len(toComp)] == toComp:
            pot.append(temp)
#            flag = temp
#            break

        if len(pot) == 1:
            flag = pot[0]
        else:
            pass
#            print(pot)

    if s == len(flag):
     #   print(encflag[-7:])
        break
    
    print(flag)




