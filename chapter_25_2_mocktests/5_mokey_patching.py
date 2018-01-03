import urllib.request

def read_webpage(url):
    response = urllib.request.urlopen(url)
    return response.read()

# we want to create a mocked version of Python’s urllib so that we can call
# our function above without actually downloading anything

from unittest.mock import patch

@patch('urllib.request.urlopen')
def dummy_reader(mock_obj):
    result = read_webpage('google.com')
    mock_obj.assert_called_with('google.com')
    print(result)

if __name__ == '__main__':
    dummy_reader()