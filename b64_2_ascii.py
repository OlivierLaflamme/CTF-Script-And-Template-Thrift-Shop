import sys
import base64

if __name__ == "__main__":
	
	uString = str(sys.argv[1])
	convStr = base64.b64decode(uString)

	print(convStr.decode('ascii'))
