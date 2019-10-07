import sys

if __name__ == "__main__":

	uHex = str(sys.argv[1])	
	uAscii = bytes.fromhex(uHex).decode('ascii')

	print(uAscii)
