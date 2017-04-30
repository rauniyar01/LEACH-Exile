import json
from message import *

#TODO: Create constant for valid data
VALID_JSON = "{'id_str': '098f6bcd4621d373cade4e832627b4f6', 'dest': '127.0.0.1:50000', 'data': 'data'}"

#TODO: Create constant for malicious data
INVALID_JSON ="{'id_str': '098f6bcd4621d373cade4e832627b4f6', 'dest': '127.0.0.1:50000', 'data': 'data'}"

exiled = []

#Check if node is exiled
def is_exiled(id_str):
    return id_str in exiled

#Receive message and forward it to the sink
def recv_and_fwd(sock, id_str, upstream_addr):
    recvd = recv_message(sock)

    #Forward the message only if the message did not come from the sender
    if recvd.id_str != upstream_addr:
        send_message(sock, id_str, upstream_addr, json.dumps(recvd))
    return recvd

def exile(node):
    global exiled
    if not is_exiled(node):
        exiled.append(node)

def welcome(node):
    global exiled
    if is_exiled(node):
        exiled.remove(node)

def exiled_list():
    global exiled
    return exiled

#Take a socket object, create a json blob, and send it
def send_message(sock, id_str, dest, data):
    
    #Build the json from the supplied data
    data = json.dumps({'id_str': id_str, 'dest': dest, 'data': data})

    #make a connection and send it to the destination
    try:
        sock.connect(dest)
        sock.send(data)
        sock.close()
    except socket.error as e:
        print "Could not send message: {}".format(e)
        return False

    return True

#Receive message and return a dictionary
#This allows you to do forward the entire message later
def recv_message(socket):
    data = sock.recv()
    return json.loads(data)

