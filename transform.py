enc=open("enc").read()
print()
print(enc[0])
print(hex(ord(enc[0])))

for c in enc:
    print(hex(ord(c).lstrip("0x"),end='')
