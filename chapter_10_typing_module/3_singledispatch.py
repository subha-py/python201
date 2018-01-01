from functools import singledispatch

@singledispatch
def add(a, b):
    raise NotImplementedError('Unsupported type')

@add.register(int)
def _(a: int,b: int)->int:
    print("First argument is of type",type(a))
    print(a + b)

@add.register(str)
def _(a:str,b:str)->str:
    print("First argument is of type",type(a))
    print(a + b)

@add.register(list)
def _(a:list,b:list)->list:
    print("First argument is of type",type(a))
    print(a + b)

if __name__ == '__main__':
    add(1,2)
    add('Python', 'Programming')
    add([1,2,3],[5,6,7])
# If we were to call our add function with something else, such as a dictionary, then it
# would raise a NotImplementedError.
    # this will print the implemented types
    print(add.registry.keys())