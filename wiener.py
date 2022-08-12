"""
MxRy - 2016 - Wiener's attack 
useful link : http://math.unice.fr/~walter/L1_Arith/cours2.pdf
"""
import math

def DevContinuedFraction(num, denum) :
    partialQuotients = []
    divisionRests = []
    for i in range(int(math.log(denum, 2)/1)) :
        divisionRests = num % denum
        partialQuotients.append(num / denum)
        num = denum
        denum = divisionRests
        if denum == 0 :
            break
    return partialQuotients

""" (cf. useful link p.2) Theorem :
p_-2 = 0 p_-1 = 1   p_n = a_n.p_n-1 + p_n-2
q_-2 = 1 q_-1 = 0   q_n = a_n.q_n-1 + q_n-2 
"""
def DivergentsComputation(partialQuotients) :
    (p1, p2, q1, q2) = (1, 0, 0, 1)
    convergentsList = []
    for q in partialQuotients :
        pn = q * p1 + p2
        qn = q * q1 + q2
        convergentsList.append([pn, qn])
        p2 = p1
        q2 = q1
        p1 = pn
        q1 = qn
    return convergentsList    

"""  
https://dzone.com/articles/cryptographic-functions-python
Be careful to physical attacks see sections below
"""
def SquareAndMultiply(base,exponent,modulus):
    binaryExponent = []
    while exponent != 0:
        binaryExponent.append(exponent%2)
        exponent = exponent/2
    result = 1
    binaryExponent.reverse()
    for i in binaryExponent:
        if i == 0:
            result = (result*result) % modulus
        else:
            result = (result*result*base) % modulus
    return result

def WienerAttack(e, N, C) :
    testStr = 42 
    C = SquareAndMultiply(testStr, e, N)
    for c in DivergentsComputation(DevContinuedFraction(e, N)) :
        if SquareAndMultiply(C, c[1], N) == testStr :
            FullReverse(N, e, c)
            return c[1]
    return -1

"""
Credit for int2Text : 
https://jhafranco.com/2012/01/29/rsa-implementation-in-python/
"""
def GetTheFlag(C, N, d) :
    p = pow(C, d, N)
    print p
    size = len("{:02x}".format(p)) // 2
    print "Flag = "+"".join([chr((p >> j) & 0xff) for j in reversed(range(0, size << 3, 8))])

"""
http://stackoverflow.com/questions/356090/how-to-compute-the-nth-root-of-a-very-big-integer
"""
def find_invpow(x,n):
    high = 1
    while high ** n < x:
        high *= 2
    low = high/2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**n < x:
            low = mid
        elif high > mid and mid**n > x:
            high = mid
        else:
            return mid
    return mid + 1

"""
On reprend la demo on cherche (p, q), avec la recherche des racines du P
de scd degre : x^2 - (N - phi(N) + 1)x + N
"""
def FullReverse(N, e, c) :
    phi = (e*c[1]-1)//c[0]
    a = 1
    b = -(N-phi+1)
    c = N
    delta =b*b - 4*a*c
    if delta > 0 :
        x1 = (-b + find_invpow((b*b - 4*a*c), 2))/(2*a)
        x2 = (-b - find_invpow((b*b - 4*a*c), 2))/(2*a)
        if x1*x2 == N :
            print "p = "+str(x1)
            print "q = "+str(x2)
        else :
            print "** Error **"
    else :
        print "** ERROR : (p, q)**"

"""
Si N, e, C en hex ::> int("0x0123456789ABCDEF".strip("0x"), 16)
"""
if __name__ == "__main__":
    C = 46915423865273804628100546915542006682162854437889203618682187985370604827457604245883183502592255149919322918128978901671162484822332561912184387238657308075842174462822845509425648544227644862671791557557932454990085055060044101986976192362621690152659566956658101523957736828267906973046968372002659612062
    e = 47841361553306331261251563567491156295558934125407951532656094200237138235562577221968246327516783612246873638084755037412292227029462168466755940963226857652943095914532993569966089908368224774586903718956004355103306096768682305379384616470253947685207371904783129192254499936604176864202620159577038047003
    N = 79864706674412023777895526894425705042779091824758017678719299934677003561158073422091341906358472637426797299580821767670421915838468219706222530901723066683690392591201018705436008712120702092660585413226705395782174752738989417010198541963465694196685839832213415497780499384345509940450423566497169314313

    print "e : "+str(e)
    print "N : "+str(N)
    print "C : "+str(C)
    d = WienerAttack(e, N, C)
    if d != -1 :
        print "d = "+str(d)
        GetTheFlag(C, N, d)
    else :
        print "** ERROR : Wiener's attack Impossible**"
