import socketserver
import os


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):

        self.data = self.request.recv(1024).strip()
        print ("{} commanded:{}".format(self.client_address[0],self.data.decode('UTF-8')))
        self.tmp=os.popen(self.data.decode('UTF-8')).read()

        # just send back the same data, but upper-cased
        self.request.sendall(bytes(self.tmp,'UTF-8'))

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    server.serve_forever()