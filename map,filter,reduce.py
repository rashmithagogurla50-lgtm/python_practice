a=(2,3,4,5)##square
print(list(map(lambda x:x*x,a)))

a=("apple","ant","cat")##convt into the uppercase using map
print(list(map(lambda x:x.upper(),a)))

a=(10,12,13,20)##even by filter
print(list(filter(lambda x:x%2==0,a)))

a=(1,-3,4,-5,-6,8,9)##positive values
print(list(filter(lambda x:x>0,a)))

from functools import reduce##sum by using reduce import
a=(10,20,30)
print(reduce(lambda x,y:x+y,a))

a=(5,10,15,20)
print