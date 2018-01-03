# The autospec allows you to create
# mock objects that contain the same attributes and methods of the objects that you are replacing
# with your mock.

from unittest.mock import create_autospec

def add(a,b):
    return a+b

mocked_func = create_autospec(add,return_value = 10)
res = mocked_func(1,2)
print(res)
try:
    mocked_func(1,2,3)
except TypeError:
    print('Since, add have two arguments, the mock object cannot take more than 2 arguments')