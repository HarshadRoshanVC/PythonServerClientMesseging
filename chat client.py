import socket
from datetime import datetime

HOST=socket.gethostname()
PORT=6789
max_size=1024

print('starting client at:',datetime.now())
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#sock.bind((HOST,PORT))
s.connect((HOST,PORT))

while True:
    msg_to_server=input('Enter msg:')
    msg_to_server_encoded=msg_to_server.encode('utf-8')
    s.send(msg_to_server_encoded)
    if msg_to_server=='q':
        break
    data=s.recv(max_size)
    if data.decode('utf-8')=='q':
        break
    print("At ",datetime.now(),' said ',data.decode('utf-8'))


s.close()
