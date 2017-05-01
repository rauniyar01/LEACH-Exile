import json
from socket import error as socketError
from parser import *
from node_management import *

########################
# Message Routing Code #
########################
#TODO: Flesh the rest of this out since we need it to work

#TODO: Forward packets to the upstream address
def forward_upstream():
    pass

#TODO: loop through all of the nodes and then call send message
#Should only be used to transmit exit or welcome messages
def forward_to_all_nodes():
    pass

#TODO: handle the routing based on the information retunred 
#from parsing the packet
def handle_routing():
    pass

#Receive message and forward it to the sink
def recv_and_fwd(sock, id_str, upstream_addr):
    recvd = recv_message(sock)

    #Forward the message only if the message did not come from the sender
    if recvd.id_str != upstream_addr:
        print "Forwarding message"
        send_message(sock, id_str, upstream_addr, json.dumps(recvd))
    return recvd

#Take a socket object, create a json blob, and send it
#Returns Boolean for success or fail
#TODO: Add logic for exiled nodes
def send_message(sock, id_str, dest, data):
    #If the node is exiled, return False
    if not node_status(dest):
        return False

    #Build the json from the supplied data
    data = json.dumps({'id_str': id_str, 'dest': dest, 'data': data})

    #make a connection and send it to the destination
    try:
        sock.connect(dest)
        sock.send(data)
        sock.close()
    except socketError as e:
        print "Could not send message: {}".format(e)
        return False

    return True

#Receive message and return a dictionary
#This allows you to do forward the entire message later
#TODO: Add logic for exiled nodes
def recv_message(sock):
    #Receive the data
    data = sock.recv(2048)
    recvd = json.loads(data)

    #If the node is exiled return the data, else return False
    if not node_status(recvd.id_str):
        return recvd
    else:
        return False

def tuple_to_socketStr(tuple):
    return '{}:{}'.format(tuple[0], tuple[1])


def socketStr_to_tuple(socketStr):
    array = socketStr.split(':')
    return array[0], array[1]

