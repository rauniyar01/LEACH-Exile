import json

VALID_JSON = "{'id_str': '098f6bcd4621d373cade4e832627b4f6', 'dest': '127.0.0.1:50000', 'data': 'valid'}"
INVALID_JSON ="{'id_str': '098f6bcd4621d373cade4e832627b4f6', 'dest': '127.0.0.1:50000', 'data': 'malicious'}"

#Addresses will be the keys
#The value will be True if active
#The value will be False if exiled
nodes = {}

#Check if node is exiled
#Change to work with dictionary
def node_status(node):
    global nodes
    if node not in nodes:
        return false
    else:
        return nodes[node]
        

#Receive message and forward it to the sink
def recv_and_fwd(sock, id_str, upstream_addr):
    recvd = recv_message(sock)

    #Forward the message only if the message did not come from the sender
    if recvd.id_str != upstream_addr:
        send_message(sock, id_str, upstream_addr, json.dumps(recvd))
    return recvd

#Change to work with dictionary
def exile(node):
    global nodes
    if node not in nodes:
        insert(node)

    nodes[node] = False

#Change to work with dictionary
def welcome(node):
    global nodes
    if not node_status(node):
        nodes[node] = True

#Change to work with dictionary
def exiled_nodes():
    global nodes
    exiled = []
    for key, val in nodes.iteritems():
        if nodes[key] == False:
            exiled.append(key)

    return exiled

#Returns a list of the welcomed nodes
def welcomed_nodes():
    global nodes
    welcomed = []
    for key, val in nodes.iteritems():
        if nodes[key] == True:
            welcomed.append(key)

    return welcomed

#Returns a list of all of the nodes
def get_nodes():
    return nodes

#Insert the node and initialize it if it's not there
def insert(node):
    global nodes
    if node not in nodes:
        nodes[node] = True
        
#Take a socket object, create a json blob, and send it
#TODO: Add logic for exiled nodes
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
#TODO: Add logic for exiled nodes
def recv_message(socket):
    data = sock.recv()
    return json.loads(data)

