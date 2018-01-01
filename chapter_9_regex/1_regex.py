# To actually do a search though, we would need to add a beginning character to look for and an
# ending character. To make this easier, we can use the asterisk which allows repetitions. Instead of
# matching *, the * will tell the regular expression that the previous character may be matched zero
# or more times.
# It always helps to see a simple example:
# ‘a[b-f]*f

# This regular expression pattern means that we are going to look for the letter a, zero or more letters
# from our class, [b-f] and it needs to end with an f.
import re
text = 'abcdfghijk'
parser = re.search('a[b-f]*f',string=text)
print(parser.group())

# * means it will match only zero or more times but + means it will match 1 or more times

# The final repeated metacharacter is {a,b} where a and b are decimal integers. What this means is that
# there must be at least a repetitions and at most b

# xb{1,4}z

# This is a pretty silly example, but what it says is that we will match things like xbz, xbbz, xbbbz
# and xbbbbz, but not xz because it doesn’t have a “b”.

# The next metacharacter that we’ll learn about is ˆ. This character will allow us to match the
# characters that are not listed inside our class. In other words, it will complement our class. This
# will only work if we actually put the ˆ inside our class. If it’s outside the class, then we will be

# attempting to actually match against ˆ. A good example would be something like this: [ˆa]. This will
# match any character except the letter ‘a’.

# The ˆ is also used as an anchor in that it is usually used for matches at the beginning of string. There
# is a corresponding anchor for the end of the string, which is $

# . will match any character without the new line