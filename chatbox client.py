import socket
print("For client side")
HOST=socket.gethostname()
PORT=12345
s=socket.socket()
s.connect((HOST,PORT))
while True:
    message=input("Ur msg: ")
    s.send(message.encode())
    if message=='end':
        break
    reply=s.recv(1024)
    print("Recieved",repr(reply))
s.close()
