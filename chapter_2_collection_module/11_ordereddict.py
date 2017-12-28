d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}
print(d)
# this is not ordered
# to loop them in order without order dict

keys = d.keys()
print(keys)

# sorted
keys = sorted(keys)
print(keys)
for key in keys:
    print(key,d[key])