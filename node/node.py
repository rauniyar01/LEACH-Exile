import socket
from multiprocessing import Process, Queue
from utilities.leach_utils import *
from sys import exit
from time import sleep


class Node:
    def __init__(self, node_type, port):
        self.node_type = node_type
        self.port = port
        self.queue = Queue()

        recvSock = self._bind('localhost', self.port)
        # Make the listening socket tuple the id_str
        self.id_str = tuple_to_socketStr(recvSock.getsockname())

        Process(target=self._listen, args=(recvSock,)).start()
        sendSock = self._bind('localhost', self.port+1)

        if node_type == 'node':
            self._node(recvSock, sendSock)
        elif node_type == 'ch':
            self.clusterhead(recvSock, sendSock)
        elif node_type == 'sink':
            self.sink(recvSock, sendSock)
        elif node_type == 'snort':
            # everything will be done in snort.py, which needs access to node class functions
            pass
        else:
            exit('[!] Error: Somehow gave wrong node_type')

    def _node(self, recvSock, sendSock):
        goodboye = raw_input('Will this node be a goodboye? (Y/n): ')

        while True:
            if not self.queue.empty():
                #data = self.queue.get()
                # Parse the data, see if a node should be added to exile list or welcomed
                pass

            if goodboye.lower() == 'y' or goodboye == '\n':
                # send(VALID_JSON) to CH
                pass
            else:
                # send(INVALID_JSON) to CH
                pass

            sleep(1)

    def clusterhead(self, recvSock, sendSock):
        while True:
            if not self.queue.empty():
                #data = self.queue.get()
                # Parse the data, see if a node should be added to exile list or welcomed.
                # If not, it probably needs to be forwarded to the sink
                pass

            sleep(1)

    def sink(self, recvSocklo, sendSocklo):
        # Used to get the IP of the main interface so that a socket can be made on it
        recvSockEns33 = self._bind(socket.gethostbyname(socket.gethostname()), self.port+1)
        sendSockEns33 = self._bind(socket.gethostbyname(socket.gethostname()), self.port+2)
        Process(target=self._listen, args=(recvSockEns33,)).start()

        # Have some data parsing based on what is in self.queue
        # If it came from CH, send/forward to Snort node
        # if it came from snort node, see if it is a welcome/exile

    def _listen(self, sock):
            sock.listen(5)
            try:
                while True:
                    client, address = sock.accept()
                    client.settimeout(60)
                    # Get Ready to recv data, Will also need to accommodate messages coming to the sink form snort.py
                    # self.queue.put(data)
            except KeyboardInterrupt:
                exit('Exitting Thread...')

    def _bind(self, ip, port):
        try:
            print "[*] Attempting to bind on port: {} with ip: {}".format(port, ip)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((ip, port))
            self.port = port
            return s

        except socket.error:
            print "[!] Error: port already in use, incrementing port from {} to {}".format(port, port+1)
            s = self._bind(ip, port+1)
            return s
