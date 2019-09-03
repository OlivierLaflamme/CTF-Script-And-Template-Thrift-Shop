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

"""This module does blah blah."""
def xor(input_string, key):
    result = ""

    for i in range(0, len(input_string) - 1, 2):
        x_ch = int(input_string[i:i+2], 16)
        result += chr(x_ch ^ ord(key))

    return result

"""This module does blah blah."""
def main():
    input_string = "98097d5a61a4906e098d96d2e5025967"

    m = ' '
    try:
        for i in range(0, 256):
            temp = xor(input_string, chr(i))
            print(temp + "\n")
    except:
        print("shit")

main()
