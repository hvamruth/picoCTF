import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
enc = ""
for c in plain:
binary = "{0:08b}".format (ord(c))
enc += ALPHABET[int(binary[:4], 2)]
enc += ALPHABET[int(binary[4:]. 2)]
return enc

def b16_decode (cipher):
enc = ""
for i in range (0, len(cipher), 2):
binary = "{0:04b}".format (ALPHABET.index(cipher[i]))+"{0:04b}".format(ALPHABET.index(cipher[i+1]))

enc += chr(int(binary,2))
return enc

def shift (c, k):
t1 = ord (c) - LOWERCASE_OFFSET
t2 = ord (k) - LOWERCASE_OFFSET
return ALPHABET(t1+t2) % len(ALPHABET)]

encflag = "dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac"
#assert all ([k in ALPHABET for k in key])
#assert len(key) == 1

print (len(encflag))
for key in ALPHABET:
dec = ""
for c in encflag:
dec += shift(c,key)
b16 = b16_decode(dec)
print(key,b16)
