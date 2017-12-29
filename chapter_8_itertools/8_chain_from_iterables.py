from itertools import chain

numbers = range(5)
cmd = ['/home/subha','/opt/bin/']
my_list = list(chain.from_iterable([['foo','bar'],cmd,numbers]))
# this takes list of list to chain..

print(my_list)
# this could be achieved by list1+ list2+ list3 too..