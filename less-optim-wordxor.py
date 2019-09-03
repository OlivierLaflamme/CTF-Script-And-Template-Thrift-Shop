#!/usr/bin/env python
#
# breaks word key xor

def score(text):
	charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!'"
	p = 0
	for s in text:
		if s in charset or s == ' ':
			p+=1
	return p

def xor(s1, s2):
	res = ""
	for i in range(0, len(s1)):
		res += chr(ord(s1[i]) ^ ord(s2[i%len(s2)]))

	return res

def main():
	text = "BREAKING THE HABIT! THIS TEXT HAS TO BE A LITTLE BIT LONGER! THIS TEXT HAS TO BE A LITTLE BIT LONGER! THIS TEXT HAS TO BE A LITTLE BIT LONGER!"
	key = "CHURCH"

	cipher = xor(text, key)

	""" NOW WE GONNA BREAK IT! WE ONLY HAVE CIPHERTEXT in variable CIPHER"""
	seckey = ""
	l = 6 # bruteforce or through hamming distance
	for s in range(0, l):
		w = ""
		for i in range(0, len(text)/l):
			w += cipher[i*l+s]

		best = ""
		b = 0
		tmpkey = ""
		for charx in range(0, 256):
			c = xor(w, chr(charx))
			if score(c) > b:
				b = score(c)
				tmpkey = chr(charx)

		seckey += tmpkey

	print "KEY: " + seckey
	print "PLAINTEXT: " + xor(cipher, seckey)


if __name__ == "__main__":
	main()
