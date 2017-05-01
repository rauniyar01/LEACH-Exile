import socket
from leach_utils import *

import SocketServer

def handle(self):
    # self.request is the TCP socket connected to the client
    self.data = self.request.recv(1024).strip()
    print "{} wrote:".format(self.client_address[0])
    print self.data
    
    #My added code
    recv_and_fwd(self, "test_id_str", ('127.0.0.1', 9998))

if __name__ == "__main__":
    HOST, PORT = "localhost", 9998

    # Create the server, binding to localhost on port 9999
    s1 = socket.socket(socket.AF_INET, socket. SOCK_STREAM)

    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.bind((HOST, PORT))
    s1.listen(1)

    conn, addr = s1.accept()
    print 'Connection address:', addr
    while 1:
        data = conn.recv(2048)
        if data:
            print "received data:", data
            conn.close()
            s1.close()
            break

    s2 = socket.socket(socket.AF_INET, socket. SOCK_STREAM)
    print "before"
    send_message(s2, "tests", (HOST, 9999), data)
    print "after"
    s2.close()
