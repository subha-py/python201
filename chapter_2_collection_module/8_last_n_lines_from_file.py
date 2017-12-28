from collections import deque


def get_last(filename, n=5):
    """
    This code works in much the same way as Linux’s tail program does.
    :param filename:
    :param n:
    :return: Return last n lines from the file
    """
    try:
        with open(filename) as f:
            return deque(f, n)
    except OSError:
        print('Error opening file : {}'.format(filename))
        raise
