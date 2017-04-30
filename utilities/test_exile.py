import leach_utils

leach_utils.exile("a")
leach_utils.exile("b")
leach_utils.exile("c")

print leach_utils.exiled_list()

leach_utils.welcome("b")

print leach_utils.exiled_list()
