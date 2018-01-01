import re

regex=re.compile('''
                    [\w\.-]+ #username
                    @
                    [\w\.-]+ #the domain
                    ''',re.VERBOSE)
print(regex)