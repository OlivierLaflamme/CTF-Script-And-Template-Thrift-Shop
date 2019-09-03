#!/usr/bin/env python
payload = ''
for i in range(0xaa,0xff):
        payload += chr(i)

print payload
