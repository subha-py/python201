from contextlib import redirect_stdout

path = '5_test_example.txt'
with open(path, 'w') as fobj:
    with redirect_stdout(fobj):
        help(redirect_stdout)