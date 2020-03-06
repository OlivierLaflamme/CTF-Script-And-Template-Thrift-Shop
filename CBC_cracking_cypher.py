import sys
import base64
from Crypto.Cipher import AES

class AESCipher(object):
  def __init__(self, pass):
    self.bs = 16
    self.cipher = AES.new(pass, AES.MODE_ECB)
 
 def decrypt(self, raw):
  decoded = base64.b64decode(raw)
  decrypted = self.cipher.decrypt(decoded)
    return str(self._unpad(decrypted)).encode("utf-8")
 
 def _unpad(self, s):
 return s[:-ord(s[len(s)-1:])]

if __name__ == '__main__':
 pass = 'LOLOLOL'
 cipher = AESCipher(pass)
 
 ciphertext ='SOMETHINGSOMETHING=='
 
 decrypted = cipher.decrypt(ciphertext)
 print('Decrypted: %s' % decrypted)
