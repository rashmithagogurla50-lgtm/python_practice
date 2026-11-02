t=(1,2,3,4)##unpacking tuple using *
x,*y=t
print(x)
print(y)

t=(1,2,3,4,5)##unpacking
x,*y,z=t
print(x)
print(y)
print(z)

##packing tuple
name="rashmitha"
blood="b"
ticket=234
student=name,blood,ticket
print(student)

a=(12,15,16)
print(a)