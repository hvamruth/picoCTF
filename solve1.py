import string

LOWERCASE_OFFSET = ord("a") 
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))
        enc += ALPHABET[int(binary[:4], 2)]
        enc += ALPHABET[int(binary[4:], 2)]
    return enc

def shift(c, k):
      t1 = ord(c) + offset
      t2 = ord(k) + offset
      return alphabet[(t1 + t2) % len(alphabet)]

def b16_decode(encoded):

    for e in encoded:
      p1 = f"{alphabet.index(encoded[:1]):04b}"
      p2 = f"{alphabet.index(encoded[1:]):04b}"



f'{ord("a"):04b}'
int(f'{ord("a"):04b}',2)


 binary = p1 +2
        char = chr(int(binary,2))

        return char
	def check(text):
	   for t in text:
             if t not in string.printable:
                return False

    return True

	ciphertext = 'dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac'

for a in alphabet:
    plain = ''
    key = a
    decode = '' 

    for i,c in enumerate(ciphertext):
        decode += shift(c, key)

    for i in range(0,len(decode),2):
        temp = (decode[i] + decode[i+1])

        plain += b16_decode(temp)

    if check(plain):
        print(f'key = {a} : {plain} ')
        print(flag) 
