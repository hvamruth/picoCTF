import socket
print("For server side")
HOST=socket.gethostname()
PORT=12345
s=socket.socket()
s.bind((HOST,PORT))
s.listen(1)
conn,addr=s.accept()
print("connected by:",addr)
while True:
    data=conn.recv(1024)
    print('received',repr(data))
    reply=input("message:")
    conn.sendall(reply.encode())
    if reply=='end':
        break
conn.close()   
