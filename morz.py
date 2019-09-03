#!/usr/python

import sys

class Morse:

	def __init__(self):
		self.morseAlphabet ={
		        "A" : ".-",
		        "B" : "-...",
		        "C" : "-.-.",
                        "D" : "-..",
		        "E" : ".",
		        "F" : "..-.",
		        "G" : "--.",
		        "H" : "....",
		        "I" : "..",
		        "J" : ".---",
		        "K" : "-.-",
		        "L" : ".-..",
		        "M" : "--",
		        "N" : "-.",
		        "O" : "---",
		        "P" : ".--.",
		        "Q" : "--.-",
		        "R" : ".-.",
		        "S" : "...",
		        "T" : "-",
		        "U" : "..-",
		        "V" : "...-",
		        "W" : ".--",
		        "X" : "-..-",
		        "Y" : "-.--",
		        "Z" : "--..",
		        " " : "/",
			"1" : ".----",
			"2" : "..---",
			"3" : "...--",
			"4" : "....-",
			"5" : ".....",
			"6" : "-....",
			"7" : "--...",
			"8" : "---..",
			"9" : "----.",
			"0" : "-----",
			"." : ".-.-.-",
			"," : "--..--",
			":" : "---...",
			"?" : "..--..",
			"'" : ".----.",
			"-" : "-....-",
			"/" : "-..-.",
			"@" : ".--.-.",
			"=" : "-...-"	
        		}
		self.flippedMorseAlphabet = flippedMorseAlphabet = dict((v,k) for k,v in self.morseAlphabet.items())

	def encode(self, str):
		encoded = ""
		for char in str:
			encoded += self.morseAlphabet[char]+" "
		return encoded

	def decode(self, str, separator=" "):
		morseList = str.split(separator)
		decoded = ""
		for morseChar in morseList:
			decoded += self.flippedMorseAlphabet[morseChar]	
		return decoded


if __name__ == '__main__':
	input = ".---- .---- .----"
	morseDecoder = Morse()
	print morseDecoder.decode(input)
	print morseDecoder.encode(morseDecoder.decode(input))
