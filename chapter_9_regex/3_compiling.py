import re

text = "The ants go marching one by one"
strings = ['the','one']

for string in strings:
    regex = re.compile(pattern=string)
    match = re.search(regex,string=text)
    if match:
        print('Found {string} in {text}'.format(string=string,text=text))
        text_pos = match.span()
        print(text_pos)
        print(text[text_pos[0]:text_pos[1]])

    else:
        print('Did not find {string}'.format(string=string))

# The primary reason to use compile is to save it to be reused later on in your
# code. However, compile also takes some flags that can used to enable various special features. We
# will take a look at that next.
# Special Note: When you compile patterns, they will get automatically cached so if you aren’t using lot
# of regular expressions in your code, then you may not need to save the compiled object to a variable.