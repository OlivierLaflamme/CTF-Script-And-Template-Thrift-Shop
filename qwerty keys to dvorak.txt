#translate qwerty keys to dvorak to get the flag I've seen this in ~4 CTF's 
#never want to write this code again

from string import maketrans

#QWERTY = '''-=qwertyuiop[]sdfghjkl;'zxcvbn,./_+QWERTYUIOP{}SDFGHJKL:"ZXCVBN<>?'''
#DVORAK = '''[]',.pyfgcrl/=oeuidhtns-;qjkxbwvz{}"<>PYFGCRL?+OEUIDHTNS_:QJKXBWVZ'''

# adjust translation slightly for {}_ symbols
QWERTY = '''-=qwertyuiop[]sdfghjkl;'zxcvbn,./_+QWERTYUIOP{}SDFGHJKL:"ZXCVBN<>?'''
DVORAK = '''_]',.pyfgcrl/=oeuidhtns-;qjkxbwvz{}"<>PYFGCRL{}OEUIDHTNS_:QJKXBWVZ'''
TRANS = maketrans(QWERTY, DVORAK)
KEY_CODES = {
4:"a", 5:"b", 6:"c", 7:"d", 8:"e", 9:"f", 10:"g", 11:"h",
12:"i", 13:"j", 14:"k", 15:"l", 16:"m", 17:"n", 18:"o", 19:"p",
20:"q", 21:"r", 22:"s", 23:"t", 24:"u", 25:"v", 26:"w", 27:"x",
28:"y", 29:"z", 30:"1", 31:"2", 32:"3", 33:"4", 34:"5", 35:"6",
36:"7", 37:"8", 38:"9", 39:"0", 40:"\n", 44:" ", 45:"-", 46:"=",
47:"{", 48:"}", 49:"|", 51:";", 54:","
}

# read in the data from text file
with open("NAMEFILE.txt") as f:
    data=f.readlines()

flag=''
for packet in data:    
    key = int(packet[4:6],16)
    if key != 0:
        if packet.startswith("20") or packet.startswith("02"):
            flag += KEY_CODES[key].translate(TRANS).upper()
        else:
            flag += KEY_CODES[key].translate(TRANS)

print flag
