from itertools import accumulate

print(list(accumulate(range(10))))
# Here we import accumulate and pass it a range of 10 numbers, 0-9. It adds each of them in turn, so
# the first is 0, the second is 0+1, the 3rd is 1+2, etc
import operator
print(list(accumulate(range(1,5), operator.mul)))

# Here we pass the number 1-4 to our accumulate iterator. We also pass it a function: operator.mul.
# This functions accepts to arguments to be multiplied. So for each iteration, it multiplies instead of
# adds (1x1=1, 1x2=2, 2x3=6, etc).
# The documentation for accumulate shows some other interesting examples such as the amortization
# of a loan or the chaotic recurrence relation. You should definitely give those examples a look as they
# are will worth your time.