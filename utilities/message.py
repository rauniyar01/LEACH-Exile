import json
import base64
from hashlib import md5
from time import time

#TODO: Send_message function
def send_message():
    """You provide it data and then it will marshall the JSON and send it
    Tell it the destination, which is previously determined through the election process"""
    pass
##TODO: Change this into a standalone function
def to_json(self):
    return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)

##TODO: Change this into a standalone function
def from_json(self, json_blob):
    """Call the decoder function, which returns a quadruple.
    Transfer the data from the quadruple into the fields of the Message"""
    msg = Message()
    msg.__dict__  = json.loads(json_blob)#, object_hook=message_decoder)
    self.id_str   = msg[0]
    self.dst_addr = msg[1]
    self.data     = msg[2]
# self.signature = msg[3]
    return msg

#NOTE: Might not need this anymore
def message_decoder(obj):
    print obj
    print type(obj)
    if '__type__' in obj and obj['__type__'] == 'Message':
        print "we're in there"
        return (obj['id_str'], obj['dst_addr'], obj['data'])#, obj['signature'])


