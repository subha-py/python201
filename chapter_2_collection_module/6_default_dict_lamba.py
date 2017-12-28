from collections import defaultdict
animal = defaultdict(lambda : 'Monkey')
animal['Sam'] = 'Tiger'
print(animal['Sam'])
print(animal['Nick'])
print(animal)