import socket

s=socket.socket()
print('server connection established..')
port=9999
s.bind(('localhost',port))
print(f'local host connected {port}')
s.listen(6)
print('Waiting for connections..')
while 1:
    c,addr=s.accept()
    print(f'connection established with {addr}')
    print(c.recv(1024).decode())
    c.send(bytes(f'{s}>Welcome to chatroom','utf-8'))
    c.close()
