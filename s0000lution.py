#!/usr/bin/env python2

from pwn import *
import string

p = remote("chal.tuctf.com", 30102)
# Level 0 - 4
for i_ in range(5):
    p.sendlineafter("Give me text:", string.ascii_uppercase[::-1])
    p.recvuntil("encrypted is ")
    mapping = dict(zip(p.recvline().strip().split(" "), string.ascii_uppercase[::-1]))
    for i in range(50):
        p.recvuntil("Decrypt ")
        encrypted = p.recvline().strip().split(" ")
        answer = ""
        for k in encrypted:
            answer += mapping[k]
        p.sendline(answer)


# Level 5
plaintext = ''.join([c * 8 for c in string.ascii_uppercase])
p.sendlineafter("Give me text:", plaintext)
p.recvuntil("encrypted is ")
mapping = {}
enc = p.recvline().strip().split(" ")
for i in range(len(enc)):
    mapping[i % 8] = mapping.get(i % 8, {})
    mapping[i % 8][enc[i]] = plaintext[i]
print mapping
for i in range(50):
    p.recvuntil("Decrypt ")
    encrypted = p.recvline().strip().split(" ")
    answer = ""
    for i, k in enumerate(encrypted):
        answer += mapping[i % 8][k]
    p.sendline(answer)

p.sendlineafter("Give me text:", "ABAB")
p.interactive()
