def add(a,b):
    """
    Returns the addition of argument: a + b

    >>> add(1,2)
    3
    >>> add(-1,10)
    9
    >>> add('a','b')
    'ab'
    """
    return a+b

if __name__ == '__main__':
    import doctest
    doctest.testmod()