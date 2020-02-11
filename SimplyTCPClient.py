import socket

host='x.x.x.x'
port=xxx

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR ,1)
s.connect((host,port))

while 1:
	data = s.recv(1024)
	print data
	if not data: break
	#Insert your treatement hear
	s.send(data)
s.close()
