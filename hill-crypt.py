#_*_coding:utf-8_*_
import sys

def format(key,plain):
    list1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    list2 = "abcdefghijklmnopqrstuvwxyz"
    keylist = []
    keynum = []
    Alist = []
    Clist = []
    i = len(plain)
    if i < 4:
        f = 2
    else:
        f = 1
    if i%(len(plain))!=0:
        print "error len of key or plaintext"
    else:
        for j in range(i):
            keylist.append(key[i*j:i*j+i])
        for y in range(i):
            for x in keylist[y]:
                if list1.find(x)>-1:
                    keynum.append(list1.find(x))
                else:
                    keynum.append(list2.find(x))
            Alist.append(keynum)
            keynum = []
        for x in plain:
            if list1.find(x) > -1:
                Clist.append(list1.find(x))
            else:
                Clist.append(list2.find(x))
        return Alist,Clist,i,f

def daiyu(n,f,A1):
    x=1
    y1=0
    y2=0
    for a in range(n - f):
        for b in range(n - 1):
            x = x * A1[(0 + b) % (n - 1)][(a + b) % (n - 1)]
        y1 = y1 + x
        x = 1
    for a in range(n - f):
        for b in range(n - 1):
            x = x * A1[(n - f - b) % (n - 1)][(a + b) % (n - 1)]
        y2 = y2 + x
        x = 1
    return y1,y2

def hanglieshi(n,f,A1):
    x=1
    y1=0
    y2=0
    for a in range(n):
        for b in range(n):
            x = x * A1[(0 + b) % (n )][(a + b) % (n)]
        y1 = y1 + x
        x = 1
    for a in range(n):
        for b in range(n):
            x = x * A1[(n  - b) % (n)][(a + b) % (n)]
        y2 = y2 + x
        x = 1
    return y1,y2

def bansui(n,f,A):
    a1 = []
    A1 = []
    af = []
    Af = []
    aa = []
    for i in range(n):
        for j in range(n):
            for l in range(n):
                for k in range(n):
                    if l != i:
                        if k != j:
                            a1.append(A[l][k])
                if len(a1) > 0:
                    A1.append(a1)
                    a1 = []
            y1,y2=daiyu(n,f,A1)
            A1 = []
            af.append(pow((-1), (i + j)) * (y1 - y2))
    m = 0
    for i in range(n):
        for j in range(n):
            aa.append(af[i + (j * n)])
        Af.append(aa)
        aa = []
    return Af

def modn(e,d,m):
    d2 = 1
    for i in range(m):
        if (i * d) % m == 1:
            d2 = i
            break
    return ((e*d2)%m)

def nijuzhen(A1,A2,n,f):
    y1,y2 = hanglieshi(n,f,A1)
    print y1,y2
    hanglie = y1-y2
    print hanglie
    hl = hanglie%26
    print hl
    for i in range(n):
        for j in range(n):
            mo = modn(A2[i][j],hl,26)
            A2[i][j] = mo
    return A2
def chengfa(Ak,AC,n):
    fin = []
    kk = 0
    ke = 0
    for i in range(n):
        for j in range(n):
            kp = Ak[i][j]*AC[kk]
            kk+=1
            ke = kp+ke
            print ke
        kk = 0
        fin.append(ke%26)
    return fin

if __name__ == '__main__':
    if len(sys.argv)<3:
        print "usage:hill key plaintext"
    else:
        key = sys.argv[1]
        plaintext = sys.argv[2]
        A,C,n,f = format(key,plaintext)
        print "the key is:"+str(A)
        print "the Cipher is:"+str(C)
        A2 = bansui(n,f,A)
        An = nijuzhen(A,A2,n,1)
        print "the key^-1 is:"+str(An)
        ciphertext = chengfa(An,C,n)
        print ciphertext
