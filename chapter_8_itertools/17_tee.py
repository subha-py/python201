from itertools import tee

data = "ABCDE"
iter1,iter2 = tee(data)
# tee defaults to two, we can deep copy them actually

for item in iter1:
    print(item)

for item in iter2:
    print(item)