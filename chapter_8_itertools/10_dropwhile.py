from itertools import dropwhile


alist = [1,2,3,4,5,6,7,8,9,10]
print(list(
    dropwhile(lambda x: x<5, alist)
))

