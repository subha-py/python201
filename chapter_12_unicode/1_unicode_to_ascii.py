u = chr(40960) + 'abcd' + chr(1972)
print(u)
try:
    u.encode('ascii')
except UnicodeEncodeError:
    print('This cannot be encode to ascii')

# shortcut
res1=u.encode('ascii','ignore')
res2=u.encode('ascii','replace')
print(res1,res2)