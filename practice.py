def num(a,b,c):##factorization in function
 import math
 d=b*b-4*a*c
 if d<0:
    print(-1)
 else:
    root1=(-b-math.sqrt(d))/(2*a)
    root2=(-b+math.sqrt(d))/(2*a)
    root1=math.floor(root1)
    root2=math.floor(root2)
    if root1>root2:
      print(root1,root2)
    else:
      print(root2,root1)
num(1,-1,2)

def num(n):##counting number digits in a number
   count=0
   while n>0:
        count=count+1
        n=n//10
   return count
n=int(input("num"))
result=num(n)
print(result)

def num(n):##sum of n numbers
   total=0
   for i in range(1,n+1):
        total=total+i
   return total
n=int(input('num'))
result=num(n)
print(result)

def num(n):##prime numbers
   if n<=1:
      return "not prime"
   for i in range(2,n):
       if n%2==0:
          return "not prime"
   return "prime"
result=num(9)
print(result)