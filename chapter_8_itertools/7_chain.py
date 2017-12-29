from itertools import chain

numbers = range(5)
cmd = ['/home/subha','/opt/bin/']
my_list = list(chain(['foo','bar'],cmd,numbers))

print(my_list)
# this could be achieved by list1+ list2+ list3 too..