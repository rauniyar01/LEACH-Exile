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
            self._node()
        elif node_type == 'ch':
            self.clusterhead()
        elif node_type == 'sink':
            self.sink()
        else:
            exit('[!] Error: Somehow gave wrong node_type')

        self._bind('localhost', self.port)

    # Function to act as
    def _node(self):
        pass

    def clusterhead(self):
        pass

    def sink(self):
        self.node_id = '0'
        # Used to get the IP of the main interface so that a socket can be made on it
        self._bind(socket.gethostbyname(socket.gethostname()), self.port)

    def _bind(self, ip, port):
        try:
            print "[*] Attempting to bind on port: {} with ip: {}".format(port, ip)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((ip, port))
            s.listen(5)
            self.port = port
            return s

        except socket.error:
            print "[!] Error: port already in use, incrementing port from {} to {}".format(port, port+1)
            s = self._bind(ip, port+1)
            return s
