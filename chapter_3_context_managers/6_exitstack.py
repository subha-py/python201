from contextlib import ExitStack

filelists = 'alist of file names you want to open consequtively'.split(' ')

with ExitStack as stack:
    file_objs = [stack.enter_context(open(file=filename)) for filename in filelists]