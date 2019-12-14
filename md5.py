# -*- coding: utf-8 -*-
import hashlib

if __name__ == "__main__":
	m = hashlib.md5("hello".encode("UTF-8"))
	data = (m.hexdigest())
	print data
