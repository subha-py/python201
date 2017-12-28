from collections import deque
import string
d=deque(string.ascii_lowercase)
for letter in d:
    print(letter)

# utilities
d.append('bork')
print(d)

d.appendleft('test')
print(d)

d.rotate(1)
# You can pass it a negative number to make the deque rotate to the left instead.
print(d)

