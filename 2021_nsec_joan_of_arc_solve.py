import binascii
import string
#Cracking RC4 messages that use weak RC4 reinitialization for each message part
#
# Rainhard Findling
# University of Applied Sciences Upper Austria, Campus Hagenberg
# 2015/03
# 
# all ciphertext message parts
#Message 1
c1 = '741277e44e01296853f4dd742ecfdb8d3ea7b7b1b548e9e450afa4088f0867b58e4e0ac9e7295bbb70038fce2835e00e2258'
#Message 2
c2 = '3162c89331345b1a159dd0c40aaf670a5582bbc4c433989e74c4a7fb62ff9667d6e4965d0c5d130ecda8db3737d2f4932624'
#Message 3
c3 = '7922b0dcc814f3567e4cf5e20bbe7a0a07d6e497ab38929579ccc7c236bdd761d8ebd85d1f222013c7b28f2625c2e4e14a35'
#Message 4
c4 = '7d56ff8e2f2545094df1dfb745b56b14498faaaac03a9982369c8df8629d8836d1e0ce0e4167784e88f68f786798f88f5b40'
#Message 5
c5 = '316acfad703b2d5626b49ac300b9661a108dbb89d52f99907ba4d512719d46eac684fbb1543e264c9c95a75e5682c9b28586'
#Message 6
c6 = '0a63c8a77766085f34e0cba755fa5b5136dceb8ec4338882369a8df8629d8836d1e0ce0e4167784888f68f786798f88f5b4d'

c1 = list(map(ord, binascii.a2b_hex(c1)))
c2 = list(map(ord, binascii.a2b_hex(c2)))
c3 = list(map(ord, binascii.a2b_hex(c3)))
c4 = list(map(ord, binascii.a2b_hex(c4)))
c5 = list(map(ord, binascii.a2b_hex(c5)))
c6 = list(map(ord, binascii.a2b_hex(c6)))
# concatenate all ciphertext parts (except last) 
ciphertext = [c1, c2, c3, c4, c5, c6]
 
# our brute forcing method
def try_keys(c):
    # each key is one byte, so 255 possibilities here
    k_ok = []
    for k in range(255):
        plaintext = [x^k for x in c] 
        # all chars of one position have to translate to chars allowed in plaintext: 41-5a, 61-7a
        ok = [(chr(p_chr) in string.printable) for p_chr in plaintext]
#        ok = [p_chr == 0x20 or p_chr >= 0x41 and p_chr <= 0x5a or p_chr >= 0x61 and p_chr <= 0x7a for p_chr in plaintext]
        if(all(ok)):
            k_ok += [k]
    return k_ok
 
# brute force all keystream positions
xor = []
for i in range(50):
    c = [x[i] for x in ciphertext]
    xor += [try_keys(c)]

#print(xor)
for i in xor:
    print(i)
# see amount of possibilities left per keystream char position
#print filter(lambda x:x[1] > 1, [(i, len(xor[i])) for i in range(len(xor))])

#print(xor)

# use "first" key
#key = [x[0] for x in xor]
key = [129, 130, 140, 141, 142, 144, 145, 147, 161, 162, 172, 173, 174, 176, 177, 179]
# adapt specific keystream positions per hand so that all plaintext is correct (could be automated)
#key[3] = xor[3][7]
#key[14] = xor[14][1]
#key[21] = xor[21][1]
#key[24] = xor[24][3]
#key[25] = xor[25][5]
#key[34] = xor[34][14]

''' 
# decode (now include last message part)
plaintext = []
for c in (ciphertext):
    t = []
    for i in range(len(c)):
        t += [chr(c[i]^key[i])]
    plaintext += t
 
print ''.join(plaintext)
for c in ciphertext:
    p = ''
    for i in range(len(key)):
        p += chr(c[i]^key[i])
    print(p)    '''
