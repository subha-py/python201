# run this code in idle or py console to see the cache in effect

import urllib.error
import urllib.request

from functools import lru_cache


@lru_cache(maxsize=24)
def get_webpage(module):
    webpage = "https://docs.python.org/3/library/{}.html".format(module)
    try:
        with urllib.request.urlopen(webpage) as request:
            return request.read()
    except urllib.error.HTTPError:
        return None


modules = ['functools', 'collections', 'os', 'sys']
for module in modules:
    page = get_webpage(module)
    if page:
        print("{} module page found".format(module))

# There is also a typed parameter that we can pass to the decorator. It is a Boolean that tells the
# decorator to cache arguments of different types separately if typed is set to True.