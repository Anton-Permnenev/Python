import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
FILEPATH=input()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(bytes(FILEPATH,('UTF-8')))
data = s.recv(BUFFER_SIZE)
s.close()
fileout=open('received.txt','w+')
fileout.write(data.decode('UTF-8').replace('\r\n','\n'))
fileout.close()
print ("received data:", data)