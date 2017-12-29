from itertools import starmap

def add(a,b):
    return a+b

for item in starmap(add,[(4,5),(10,11)]):
    print(item)

# diff betw. map and starmap is func(*c) and function(a,b)