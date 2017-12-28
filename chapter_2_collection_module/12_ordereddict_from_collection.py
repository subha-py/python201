from collections import OrderedDict


d = dict(banana=3, apple=4, pear=1, orange=2)
new_d = OrderedDict(sorted(d.items()))
print(new_d)
for key in new_d:
    print(key,new_d[key])

# Note that if you add new keys, they will be added to the end of the OrderedDict instead of being
# automatically sorted.

# Something else to note about OrderDicts is that when you go to compare two OrderedDicts, they
# will not only test the items for equality, but also that the order is correct. A regular dictionary only
# looks at the contents of the dictionary and doesn’t care about its order.

# Finally, OrderDicts have two new methods in Python 3: popitem and move_to_end. The popitem
# method will return and remove a (key, item) pair. The move_to_end method will move an existing
# key to either end of the OrderedDict. The item will be moved right end if the last argument for
# OrderedDict is set to True (which is the default), or to the beginning if it is False.

# reverse a dict
print('---Reversed---')
for key in reversed(new_d):
    print(key, new_d[key])