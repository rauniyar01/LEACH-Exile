from leach_utils import *

insert("a")
insert("b")
insert("c")

print get_nodes()

exile("a")
exile("b")
exile("c")

exile("d")
print get_nodes()

welcome("b")

print get_nodes()

print "before"
print exiled_nodes()
print "after"
print welcomed_nodes()
