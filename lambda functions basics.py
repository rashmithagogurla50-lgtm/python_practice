square=lambda n :n*n
print(square(6))
cube=lambda n:n**n
print(cube(3))

add=lambda a,b:a+b
print(add(10,3))

subtract=lambda a,b:a-b
print(subtract(10,3))

multiply=lambda a,b:a*b
print(multiply(10,3))

divide=lambda a,b:a/b
print(divide(4,2))

larger=lambda a,b:a if a>b else b
print(larger(10,3))

even=lambda a:"even" if a%2==0 else "odd"
print(even(5))

check=lambda a:"positive"if a>0 else "negative" if a<0 else"zero"
print(check(3))
