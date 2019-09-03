#the cipher must be a file called 'cipher placed in the same directory'
#Enter the p,q,e and n values.
p = long(9091213529597818878440658302600437485892608310328358720428512168960411528640933367824950788367956756806141)
q = long(8143859259110045265727809126284429335877899002167627883200914172429324360133004116702003240828777970252499)
n = long('E1341893FE6E6816CEC8A970A39C00FA547C7DA2CDEDAB0A62B91C4651A83F96380BCFAEE26F7E866107906389421B1E68D0A17AADC9870B9858E956286E3999E98CEC9881534AC772AE78F5E8ABA1E2F8D3039577029D87',16)
e = 65537

phi = (p-1)*(q-1)

def sq(a):
    return a*a
def s2n(s):
    """
    String to number.
    """
    if not len(s):
        return 0
    return int(s.encode("hex"), 16)


def n2s(n):
    """
    Number to string.
    """
    s = hex(n)[2:].rstrip("L")
    if len(s) % 2 != 0:
        s = "0" + s
    return s.decode("hex")

def inverse(a, n):
    t = 0
    newt = 1    
    r = n
    newr = a    
    while newr != 0 :
        quotient = r / newr
        t, newt = (newt, t - quotient * newt) 
        r, newr = (newr, r - quotient * newr)
    if r > 1:
        print "error"

    if t < 0:
        t = t + n
    return t

def decode(c,d, n):
    """This function asks for a number and decodes it using 'd' and 'n'."""
    return pow(c, d, n)


def powmy(a,b,c):
    x=1
    y=a
    while b>0 :
        if b%2 == 1:
            x = (x * y)%c
        y= (y*y)%c
        b/=2
    return x%c

d = inverse(e,phi)
orig = s2n(open("cipher").read().rstrip())
print n2s(decode(orig,d,n))
