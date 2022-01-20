#client side
from socket import socket

enroll = 180130107086
import time
print(enroll)
print(time.ctime())
#P7_client
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.11"
port = 1234
s.connect((host,port))
def ts(str):
    s.send(str.encode())
    data = s.recv(1024).decode()
    print ("Server: ",data)
print('Start The Conversation by sending a message')
while 2:
    r = str(input('Reply: '))
    ts(r)
s.close ()