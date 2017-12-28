from collections import Counter
counter = Counter('superfluous')
print(counter.get('u'))
print(list(counter.elements()))
# top recurring two items
print(counter.most_common(2))

# example of subtract
counter_2 = Counter('super')
counter.subtract(counter_2)
print(counter.get('u'))