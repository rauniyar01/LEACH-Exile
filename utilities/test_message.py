from message import Message

def debug(message):
    print "DEBUG> {}".format(message)

debug("Creating msg1 with supplied values")
msg1 = Message('4', 'testing', "Test data is put here")

print msg1.id_str
print msg1.dst
print msg1.data

debug("Creating json from msg1")
json = msg1.to_json()
print json

debug("Creating msg 2 as a blank Message")
msg2 = Message()

debug("Loading msg2 with json from msg1")
msg2.from_json(json)
print msg2.id_str
print msg2.dst
print msg2.data
