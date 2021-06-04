import socket
from datetime import datetime

s = socket.socket()
host = 'localhost'

port = 5000

s.bind((host,port))
s.listen(5)

while True:
    c, addr = s.accept()
    print('Message from', addr)

    a = 0
    while True:
        a = a + 1
        c.send(bytes(input('Enter message: '), 'utf-8'))
        z = c.recv(2024).decode()
        print(z, datetime.now())




