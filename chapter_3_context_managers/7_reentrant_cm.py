# reentrant meaning inwards

from contextlib import contextmanager

@contextmanager
def single():
    print('Yielding')
    yield
    print('Exiting context manager')

# this will work

with single() as cm:
    pass

with single() as cm:
    pass


# this will not
cm = single()

with cm:
    pass
# this line will not yield
with cm:
    pass

# Most context managers that you create will be written such that they can only be used once using
# a with statement.