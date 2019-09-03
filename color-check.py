import re
from collections import Counter

html = open("ctfcoco_weird.htm").read()

regex = "CoCo\d+ Co"

all_colors_html = open("ctfcoco_colors.htm").read()

all_colors = re.findall(regex, all_colors_html)


used_colors=  re.findall(regex, html)

print used_colors
print Counter(used_colors)


# print all_colors.symmetric_difference(used_colors)
