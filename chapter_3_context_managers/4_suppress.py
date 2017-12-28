# with open('anyfilename.txt') as fh:
#     for line in fh:
#         print(line)
#     # this will give error since no file of such name exists


from contextlib import suppress

# this cm is reentrant
with suppress(FileNotFoundError):
    with open('anyfilename.txt') as obj:
        for line in obj:
            print(line)