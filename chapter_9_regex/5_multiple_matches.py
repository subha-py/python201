import re
silly_string = "the cat in the hat"
pattern = 'the'
match = re.findall(pattern=pattern,string=silly_string)
print(match)

# preferred way
for match in re.finditer(pattern,silly_string):
    s="Found '{group}' at {begin} : {end}".format(
        group=match.group(),
        begin=match.start(),
        end=match.end()
    )
    print(s)