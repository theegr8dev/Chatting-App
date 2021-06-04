import socket
from datetime import datetime

c = socket.socket()
host = 'localhost'
port = 5000

c.connect((host,port))

z = 0
while True:
    z = z + 1
    re = c.recv(1024).decode()
    print(re, datetime.now())
    c.send(bytes(input('Enter message: '), 'utf-8'))
    if re == 'Done':
        break
