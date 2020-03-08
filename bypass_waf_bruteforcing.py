import requests
import re
import json

url = 'http:///api/'

while 1:
    payload = raw_input('Payload : ')
    pattern = re.compile(r'([0-9a-f]{2})')
    payload = pattern.sub(r"\\u00\1", payload.encode('hex'))
    print('[+] Sending payload : {0}'.format(payload))
    r = requests.post(url, data='{"name": "' + payload+ '"}', headers={'Content-Type':'application/json;charset=utf-8'})
    print(r.text)
