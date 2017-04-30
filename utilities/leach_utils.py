import json
from message import *

exiled = []

#Check if node is exiled
def is_exiled(id_str):
    return id_str in exiled

#Receive message and forward it to the sink
def recv_and_fwd(sock, id_str, upstream_addr):
    recvd = recv_message(sock)
    send_message(sock, id_str, upstream_addr, json.dumps(recvd))

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
