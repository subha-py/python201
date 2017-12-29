from itertools import islice,count

for i in islice(count(10), 5):
    print(i)
    
# But it doesn’t mean
# “stop when I reach the number 5”. Instead, it means “stop when we’ve reached five iterations”.