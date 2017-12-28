from functools import singledispatch
from decimal import Decimal

@singledispatch
def add(a, b):
    raise NotImplementedError('Unsupported type')

@add.register(float)
@add.register(Decimal)
def _(a,b):
    print("First argument is of type",type(a))
    print(a + b)

if __name__ == '__main__':
    add(1.23,5.5)
    add(Decimal(100.5),Decimal(10.789))

# If we were to call our add function with something else, such as a dictionary, then it
# would raise a NotImplementedError.
    # this will print the implemented types
    print(add.registry.keys())