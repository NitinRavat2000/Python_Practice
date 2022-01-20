from functools import *

evens= list(filter(lambda n:n%2==0,[2,9,6,7,4,6]))

print(evens)

doubles=list(map(lambda n:n+2,evens))

print(doubles)

sum=reduce(lambda a,b: a+b,doubles)

print(sum)
