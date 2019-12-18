#!/usr/bin/python
from scapy.all import *
 
KEY_CODES = {
4:"A",
5:"B",
6:"C",
7:"D",
8:"E",
9:"F",
10:"G",
11:"H",
12:"I",
13:"J",
14:"K",
15:"L",
16:"M",
17:"N",
18:"O",
19:"P",
20:"Q",
21:"R",
22:"S",
23:"T",
24:"U",
25:"V",
26:"W",
27:"X",
28:"Y",
29:"Z",
30:"1",
31:"2",
32:"3",
33:"4",
34:"5",
35:"6",
36:"7",
37:"8",
38:"9",
39:"0",
40:"\n",
44:" ",
45:"-",
46:"=",
47:"{",
48:"}",
}
 
pkts = rdpcap("4c27525e7a3d2e45495c6284386b4d5c.cap")
msg= ""
for packet in pkts:
    global msg
    hid_report = packet.load[-8:]
    key_code = ord(hid_report[2])
    ch = KEY_CODES.get(key_code, False)
    if ch:
        msg += ch
 
print msg
