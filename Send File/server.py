import socket

def filechg(filepath):
    f = open(filepath, 'r')
    fileout=open('fileout.txt','w+')
    lines=f.readlines()
    for i in lines:
        if i=='111\n':
            fileout.write('changed\n')
        else:
            fileout.write(i)
    f.close()
    fileout.close()
    return fileout






TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ('Connection address:', addr)
while 1:
    filepath = conn.recv(BUFFER_SIZE)
    if not filepath: break
    filechg(filepath)
    sendfile = open('fileout.txt', 'rb')
    data = sendfile.read()
    conn.sendall(data)
    sendfile.close()
conn.close()
s.close()