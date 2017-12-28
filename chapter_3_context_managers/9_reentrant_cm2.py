from contextlib import redirect_stdout
from io import StringIO

stream = StringIO()

write_to_stream = redirect_stdout(stream)

with write_to_stream:
    print('Write something to the stream..')
    with write_to_stream:
        print('Write something else to stream')

print(stream.getvalue())

# Please also note that reentrant context managers
# are not necessarily thread-safe