from itertools import cycle

polys = ['triangle','square','pentagon','rectangle']
iterator = cycle(polys)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))