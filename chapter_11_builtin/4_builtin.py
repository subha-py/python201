def doubler(x):
    return x*2

alist = [1,2,3,4,5,6,7,8,9]

for num in map(doubler,alist):
    print(num)