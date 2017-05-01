from leach_utils import *

def debug(s):
    print "Debug> {}".format(s)

good = ('127.0.0.1', 4444)
bad  = ('127.0.0.1', 5555)

insert(good)
insert(bad)

print get_nodes()

exile(bad)
print get_nodes()

print welcomed_nodes()
print exiled_nodes()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.binds
