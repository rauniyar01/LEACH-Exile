import json
import base64
from hashlib import md5
from time import time

# TODO: Create Messsage class
class Message(object):

    def __init__(self, id_str, dst, data, signature):
        # Time is sufficient for entropy since it is just needs to be unique, not crypto related
        if not id_str:
            self.id_str = md5().hexdigest(time())
        else:
            self.id_str = id_str

        self.dst  = dst      # IP:port address of the destination
        self.data = data     # Data of the message being sent
        # self.signature = self.sign()

    # TODO: Convert Message object to JSON blob
    def to_json(self):
        json.dumps(self, default=lambda o: o.__dict__,
                sort_keys=True, indent=4)

    # TODO: Parse JSON blob into Message object
    def from_json(self, json_blob):
        """Call the decoder function, which returns a quadruple.
        Transfer the data from the quadruple into the fields of the Message"""
        msg = json.loads(json_blob, object_hook=message_decoder)
        self.id_str   = msg[0]
        self.dst_addr = msg[1]
        self.data     = msg[2]
        # self.signature = msg[3]

    #TODO: Sign message
    #def sign(self, key):
    #    """Key will be passed in by the caller.
    #    This is determined by whether the node is a node or the sink"""

    #    #Create a signer with SHA512
    #    signer = key.signer(
    #        padding.PSS(
    #            mgf=padding.MGF1(hashes.SHA512()),
    #            salt_length=padding.PSS.MAX_LENGTH
    #        ),
    #        hashes.SHA512()
    #    )

    #    signer.update(self.id_str)
    #    signer.update(self.dst)
    #    signer.update(self.data)
    #    self.signature = m.finalize()

    ##TODO: Verify message with crypto
    #def verify(self, key):
    #    """Returns boolean of verification status"""
    #    verifier = key.verify(
    #        self.signature,
    #        padding.PSS(
    #            mgf=padding.MGF1(hashes.SHA256()),
    #            salt_length=padding.PSS.MAX_LENGTH
    #        ),
    #    )
    #    verifier.update(self.id_str)
    #    verifier.update(self.dst)
    #    verifier.update(self.data)

    #    return verifier.verify()

    ##TODO: Sign and send message if the node is a sink
    #def sign_and_send(self, key):
    #    """Key will be passed in by the caller.
    #    This is determined by whether the node is a node or the sink"""
    #    pass


def message_decoder(obj):
    if '__type__' in obj and obj['__type__'] == 'Message':
        return (obj['id_str'], obj['dst_addr'], obj['data'])#, obj['signature'])


#TODO: Send_message function
# Probably shouldn't be a method of the Message class
def send_message():
    """You provide it data and then it will marshall the JSON and send it
    Tell it the destination, which is previously determined through the election process"""
    pass
