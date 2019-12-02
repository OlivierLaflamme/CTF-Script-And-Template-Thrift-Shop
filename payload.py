from urllib.parse import urlsplit,urlunsplit, unquote
from urllib import parse

url = "file:////def"
parts = parse.urlsplit(url)
print(parts)

url2 = urlunsplit(parts)
parts2 = parse.urlsplit(url2)

print(parts2)
