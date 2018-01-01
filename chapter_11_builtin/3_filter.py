def less_than_ten(x):
    return x < 10

my_list = [1,2,3,4,5,67,88]
for item in filter(less_than_ten,my_list):
    print(item)

# there is also a filterfalse in itertools

