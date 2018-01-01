import re

text = "The ants go marching one by one"
strings = ['the','one']

for string in strings:
    match = re.search(pattern=string,string=text)
    if match:
        print('Found {string} in {text}'.format(string=string,text=text))
        text_pos = match.span()
        print(text_pos)
        print(text[text_pos[0]:text_pos[1]])

    else:
        print('Did not find {string}'.format(string=string))


# d matches digits
# D mathes not digits
# w matches alphanumeric
# W matches non-alphanumeric
# s matches spaces
# S matches non spaces

# You can use these escape codes inside of a character class, like so: [\d] . This would
# allow us to find any digit and is the equivalent of [0-9]