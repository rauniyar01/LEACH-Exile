#Addresses will be the keys
#The value will be True if active
#The value will be False if exiled
nodes = {}

########################
# Node Management Code #
########################

#Check if node is exiled
#Change to work with dictionary
def node_status(node):
    global nodes
    if node not in nodes:
        return False
    else:
        return nodes[node]
        

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

#Returns a dict of all of the nodes
def get_nodes():
    return nodes

#Insert the node and initialize it if it's not there
def insert(node):
    global nodes
    if node not in nodes:
        nodes[node] = True
