from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('http://www.google.com')) as webpage:
    for line in webpage:
        # process the line
        pass

# This will cause the handle to
# the web page to be closed once we fall out of the with statement’s code block.