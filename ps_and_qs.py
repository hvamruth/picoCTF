# from https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd (a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x -(b // a)* y, y)

def modinv (a, m):
                 g,y,x = egcd (a, m)

if g ! = 1:
    raise Exception('modular inverse does not exist')
else:
    return x % m

p=1955175890537890492055221842734816092141
q=670577792467509699665091201633524389157003 

n=p*q
phi=(p-1)*(q-1)

e=65537
d=modinv(e,phi)
c=861270243527190895777142537838333832920579264010533029282104230006461420086153423
plain=pow(c,d,n)
print (plain)
print (hex(plain))
print (bytearray.fromhex(hex(plain)[2:]).decode())
