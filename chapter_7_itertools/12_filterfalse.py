from itertools import filterfalse


alist = [1,2,3,4,5,6,7,8,9,10]

def greater_than_five(x):
    return x > 5

print(list(
    filterfalse(greater_than_five,reversed(alist))
))

# unlike dropwhile filterfalse will check each and every element
