from sys import exit, path
path.append("/home/bojak/LEACH-Exile/utilities")
from multiprocessing import Process, Queue
from utilities.leach_utils import *
from utilities.node_management import *
from utilities.parser import *
from time import sleep


class Node:
    def __init__(self, node_type, port):
        self.node_type = node_type
        self.port = port
        self.queue = Queue()
	insert('localhost:50000')
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
	sendSock = self._bind('localhost', self.port+1)
	insert('localhost:50002')
	print get_nodes()
        print send_message(sendSock, socketStr_to_tuple('localhost:50002'),
                     vals_to_json(self.id_str, 'welcome', self.id_str))
        try:
            while True:
                if not self.queue.empty():
		    sendSock = self._bind('localhost', self.port+1)

                    data = self.queue.get()
                    j = data
                    if j['data']['cmd'] == 'welcome':
                        insert(j['data']['data'])
                        welcome(j['data']['data'])
                    elif j['data']['cmd'] == 'exile':
                        exile(j['data']['data'])
                    if goodboye.lower() == 'y' or len(goodboye) == 0:
                        send_message(sendSock, socketStr_to_tuple('localhost:50002'), str_to_json(VALID_DATA))
                    else:
                        send_message(sendSock, socketStr_to_tuple('localhost:50002'), str_to_json(MALICIOUS_DATA))

                    sendSock.close()
                print get_nodes()
                sleep(1)
        except KeyboardInterrupt:
            exit('Exiting Node.py...')

    def clusterhead(self, recvSock):
        try:
            while True:
                if not self.queue.empty():
                    data = self.queue.get()
                    j  = data

                    sendSock = self._bind('localhost', self.port+1)
                    if j['data']['cmd'] == 'welcome':
                        insert(j['data']['data'])
                        welcome(j['data']['data'])
                        send_to_all_nodes(vals_to_json(self.id_str, 'welcome', j['data']['data']))
                    elif j['data']['cmd'] == 'exile':
                        exile(j['data']['data'])
                        send_to_all_nodes(vals_to_json(self.id_str, 'exile', j['data']['data']))
                    elif j['data']['cmd'] == 'data':
                        print send_message(sendSock, socketStr_to_tuple('localhost:50000'),
                                     vals_to_json(self.id_str, 'forward', j['data']['data'], orig_source=j['data']['id_str']))

                    sendSock.close()
                    print get_nodes()
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
                    j = data

                    sendSock = self._bind('localhost', self.port+1)
                    if j['data']['cmd'] == 'welcome':
                        insert(j['data']['data'])
                        welcome(j['data']['data'])
                        send_message(sendSock, socketStr_to_tuple('localhost:50002'),
                                     vals_to_json(self.id_str, 'welcome', j['data']['data']))
                    elif j['data']['cmd'] == 'exile':
                        exile(j['data']['data'])
                        send_message(sendSock, socketStr_to_tuple('localhost:50002'),
                                     vals_to_json(self.id_str, 'exile', j['data']['data']))
                    elif j['data']['cmd'] == 'forward':
                        send_message(sendSock, socketStr_to_tuple(
                            '{}:{}'.format(socket.gethostbyname(socket.gethostname()[0]), '13337')),
                                     vals_to_json(self.id_str, 'forward', j['data']['data'], orig_source=j['data']['id_str']))

                    sendSock.close()
                    print get_nodes()
                sleep(1)
        except KeyboardInterrupt:
            exit('Exiting Node.py...')

    def _listen(self, sock):
            sock.listen(5)
            try:
                while True:
                    new_sock, ip = sock.accept()
		    data = recv_message(new_sock)
                    self.queue.put(data)
		    
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
