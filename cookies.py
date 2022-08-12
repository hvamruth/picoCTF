from base64 import b64decode
from base64 import b64encode
import requests

def bitFlip( pos, bit, data):
    raw = b64decode(data)

    list1 = list(raw)
    list1[pos] = chr(ord(list1[pos])^bit)
    raw = ''.join(list1)
    return b64encode(raw)

ck = "dnAzVzl0NStWTGpOb0U5RUdaSXoyV3htbmdVdEo0d2R6SGU2OG5IR1JTSE1GcmpSN01XQnBWTldLZnZhS3hKQTZCR0FnUGxIRmVJUFBVUXBVSlBMWFRnb0FyRVlvQmFRYVBwNjRPUllRZ2dOeElQTzdvSVdkViszVG9keFdLRWs="

for i in range(128):
    for j in range(128):
        c = bitFlip(i, j, ck)
        cookies = {'auth_name': c}
        r = requests.get('http://mercury.picoctf.net:34962/', cookies=cookies)
        if "picoCTF{" in r.text:
            print(r.text)
            break
