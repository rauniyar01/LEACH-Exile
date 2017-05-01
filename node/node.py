from sys import exit, path
path.append("../utilities")
from multiprocessing import Process, Queue
from utilities.leach_utils import *
from utilities.parser import *
from utilities.node_management import *
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

        if node_type == 'node':
            self._node(recvSock)
        elif node_type == 'ch':
            self.clusterhead(recvSock)
        elif node_type == 'sink':
            self.sink(recvSock)
        elif node_type == 'snort':
            # everything will be done in snort.py, which needs access to node class functions
            pass
        else:
            exit('[!] Error: Somehow gave wrong node_type')

    def _node(self, recvSock):
        goodboye = raw_input('Will this node be a goodboye? (Y/n): ')
        try:
            while True:
                if not self.queue.empty():
                    data = self.queue.get()
                    j = str_to_json(data)

                    if j['cmd'] == 'welcome':
                        welcome(j['data'])
                    elif j['cmd'] == 'exile':
                        exile(j['data'])
                        print get_nodes()

                    sendSock = self._bind('localhost', self.port+1)
                    if goodboye.lower() == 'y' or goodboye == '\n':
                        send_message(sendSock, socketStr_to_tuple('localhost:50001'), VALID_DATA)
                    else:
                        send_message(sendSock, socketStr_to_tuple('localhost:50001'), MALICIOUS_DATA)

                    sendSock.close()
                sleep(1)
        except KeyboardInterrupt:
            exit('Exiting Node.py...')

    def clusterhead(self, recvSock):
        try:
            while True:
                if not self.queue.empty():
                    data = self.queue.get()
                    j = str_to_json(data)

                    sendSock = self._bind('localhost', self.port+1)
                    if j['cmd'] == 'welcome':
                        welcome(j['data'])
                        send_to_all_nodes(vals_to_json(self.id_str, 'welcome', j['data']))
                    elif j['cmd'] == 'exile':
                        exile(j['data'])
                        send_to_all_nodes(vals_to_json(self.id_str, 'exile', j['data']))
                    elif j['cmd'] == 'data':
                        send_message(sendSock, socketStr_to_tuple('localhost:50000'),
                                     vals_to_json(self.id_str, 'forward', j['data'], orig_source=j['id_str']))

                    sendSock.close()
                sleep(1)
        except KeyboardInterrupt:
            exit('Exiting Node.py...')

    def sink(self, recvSocklo):
        # Used to get the IP of the main interface so that a socket can be made on it
        recvSockEns33 = self._bind(socket.gethostbyname(socket.gethostname()), self.port+1)
        Process(target=self._listen, args=(recvSockEns33,)).start()
        try:
            while True:
                if not self.queue.empty():
                    data = self.queue.get()
                    j = str_to_json(data)

                    sendSock = self._bind('localhost', self.port+1)
                    if j['cmd'] == 'welcome':
                        welcome(j['data'])
                        send_message(sendSock, socketStr_to_tuple('localhost:50001'),
                                     vals_to_json(self.id_str, 'welcome', j['data']))
                    elif j['cmd'] == 'exile':
                        exile(j['data'])
                        send_message(sendSock, socketStr_to_tuple('localhost:50001'),
                                     vals_to_json(self.id_str, 'exile', j['data']))
                    elif j['cmd'] == 'forward':
                        send_message(sendSock, socketStr_to_tuple(
                            '{}:{}'.format(socket.gethostbyname(socket.gethostname()[0]), '13337')),
                                     vals_to_json(self.id_str, 'forward', j['data'], orig_source=j['id_str']))

                    sendSock.close()
                sleep(1)
        except KeyboardInterrupt:
            exit('Exiting Node.py...')

    def _listen(self, sock):
            sock.listen(5)
            try:
                while True:
                    new_sock = sock.accept()
                    self.queue.put(recv_message(new_sock))
                    new_sock.close()
            except KeyboardInterrupt:
                exit('Exiting Thread...')

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
