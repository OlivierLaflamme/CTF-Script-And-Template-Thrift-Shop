"""This module does blah blah."""
from collections import Counter
import string

"""This module does blah blah."""


def most_frequent(input_string):
    frequency = Counter()
    data = input_string
    for ch in data:
        frequency[ch] += 1

    c = frequency.most_common(10)[0][0]
    return c


def xor(input_string, key):
    result = ""

    for i in range(0, len(input_string) - 1, 2):
        x_ch = int(input_string[i:i + 2], 16)
        result += chr(x_ch ^ ord(key))

    return result


def main():
    input_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

    m = ' '
    try:
        for i in range(0, 256):
            temp = xor(input_string, chr(i))
            print(temp + "\n")
    except:
        print("shit")


main()
