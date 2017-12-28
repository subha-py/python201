# this example is from github2 package

try:
    # For Python 3
    from http.client import responses
except ImportError: # For Python 2.5-2.7
    try:
        from httplib import responses # NOQA
    except ImportError: # For Python 2.4
        from BaseHTTPServer import BaseHTTPRequestHandler as _BHRH
        responses = dict([(k, v[0]) for k, v in _BHRH.responses.items()])


# this example is from lxml
try:
    from urlparse import urljoin
    from urllib2 import urlopen
except ImportError:
    # Python 3
    from urllib.parse import urljoin
    from urllib.request import urlopen