from itertools import compress
letters = 'ABCDEFG'
bools = [True,False,True,False,True,True]
print(list(compress(letters,bools)))