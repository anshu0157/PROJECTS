import socket
c=socket.socket()
print('client connected..')
c.connect(('localhost',9999))
user_in=input()
c.send(bytes(user_in,'utf-8'))
print(c.recv(1024).decode())
print('message recieved')
