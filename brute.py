'''
4-byte magic: CTF3
4-byte name len
x-byte filename
16-byte hash:md5(md5(pwd))
4-byte data len
y-byte data
'''

from Crypto.Hash import MD5 
from itertools import product
from string import digits
from binascii import unhexlify
import pdb

dic = product(digits, repeat = 8)
# dic = product('20160610', repeat = 8)
for i in dic:
    s = ''.join(i)
    print(s)
    # print(s, i, type(i))
    m1 = MD5.new(s)
    m2 = MD5.new(unhexlify(m1.hexdigest()))
    h = unhexlify(m2.hexdigest())

    # 48 B1 ED 05 8D F7
    if h.endswith('\x48\xb1\xed\x05\x8d\xf7'):
        # 3b f3 e0 db 13 81 74 0f-96 21 48 b1 ed 05 8d f7 
        print("Found it : {} - {}".format(s, m2.hexdigest()))
        exit()
