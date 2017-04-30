import json
import socket

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
