from itertools import dropwhile


alist = [1,2,3,4,5,6,7,8,9,10]

def greater_than_five(x):
    return x > 5

print(list(
    dropwhile(greater_than_five,reversed(alist))
))