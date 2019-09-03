import string

def xor(string1, string2):
    result = ""
    
    for i in range(0, len(string1) - 1, 2):
        a = int(string1[i:i+2], 16)
        b = int(string2[i:i+2], 16)
        result += chr(a ^ b)

    return result

def main():

    string1 = "42696c6c792c20646f6e27"
    string2 = "742062652061206865726f"
    print(xor(string1, string2))

main()
