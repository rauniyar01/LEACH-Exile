import json
import socket
from parser import *
from node_management import *

#Loop through all of the nodes and then call send message
#Should only be used to transmit exile or welcome messages
def send_to_all_nodes(self_id_str, data):
    targets = welcomed_nodes()
    for target in targets:
	if self_id_str == target:
	    continue
        dest = socketStr_to_tuple(target)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        send_message(sock, dest, data)

#Take a socket object, create a json blob, and send it
#Returns Boolean for success or fail
#Add logic for exiled nodes
def send_message(sock, dest, data):
    #If the node is exiled, return False
    if not node_status(tuple_to_socketStr(dest)):
        return False

    try:
        sock.connect(dest)
        sock.send(json.dumps(data))
        sock.close()
    except socket.error as e:
        print "Could not send message: {}".format(e)
        return False

    return True

#Receive message and return a dictionary
#This allows you to do forward the entire message later
def recv_message(sock):
    #Receive the data
    data = sock.recv(2048)
    recvd = str_to_json(data)
    print recvd
    #If the node is exiled return the data, else return False
    if not node_status(recvd['id_str']):
        return recvd
    else:
        return False

def tuple_to_socketStr(_tuple):
    return '{}:{}'.format(_tuple[0], _tuple[1])


def socketStr_to_tuple(socketStr):
    array = socketStr.split(':')
    return array[0], int(array[1])

