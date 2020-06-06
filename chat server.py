import socket
from datetime import datetime
HOST=socket.gethostname()
PORT=6789
max_size=1024

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((HOST,PORT))

print('Starting the server at: ',datetime.now())
print('waiting for the incoming connection from client..')

sock.listen(5)
client, addr=sock.accept()

while True:
    data=client.recv(max_size)
    if data.decode('utf-8')=='q':
        break
    print("At ",datetime.now(),addr,' said ',data.decode('utf-8'))
    msg_to_client=input('Enter msg:')
    msg_to_client_encoded=msg_to_client.encode('utf-8')
    client.send(msg_to_client_encoded)
    if msg_to_client=='q':
        break

client.close()
sock.close()
    
