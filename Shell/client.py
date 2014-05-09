import socket

HOST, PORT = "localhost", 9999
data = input()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n",'UTF-8'))


    received = sock.recv(1024)
finally:
    print ("Command:     {}".format(data))
    print ("Received: {}".format(received.decode('UTF-8')))
    sock.close()

