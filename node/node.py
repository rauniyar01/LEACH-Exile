import socket
from utilities.message import *
from time import time
from hashlib import md5
from sys import exit


class Node:
    def __init__(self, node_type, port):
        self.node_type = node_type
        self.port = port

        # md5 used for uniqueness, not crypto. Time is fine to seed
        self.node_id = md5(str(time())).hexdigest()

        if node_type == 'node':
            self._node(self.port)
        elif node_type == 'ch':
            self.clusterhead(self.port)
        elif node_type == 'sink':
            self.node_id = '0'
            self.sink(self.port)
        else:
            exit('[!] Error: Somehow gave wrong node_type')

        self._bind(port)

    # Function to act as
    def _node(self, port):
        pass

    def clusterhead(self, port):
        pass

    def sink(self, port):
        pass

    def _bind(self, port):
        try:
            print "[*] Attempting to bind on port: {}".format(port)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(('localhost', port))
            s.listen(5)
            return s

        except socket.error:
            print "[!] Error: port already in use, incrementing port from {} to {}".format(port, port+1)
            s = self._bind(port+1)
            return s
