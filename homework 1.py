weight=float(input("weight"))## weight can be found by using bmi formula
height=float(input("height"))
bmi=weight/(height*height)
if bmi<18.5:
    print("underweight")
elif bmi<=24.9:
    print("normal")
elif bmi<=29.9:
    print("overweight")
else:
    print("obese")

a=int(input("side 1"))##triangle formation nested condition
b=int(input("side 2"))
c=int(input("side 3"))
if a+b>c and a+c>b and b+c>a:## check wheather it can form triangle or not
    print("forms triangle")
    if a==b==c:
        print("equilatorial")## if yes write this condition
    elif a==b or a==c or b==c:
        print("isosceles")
    else:
        print("scalene")
else:
    print("not form triangle")

expression=input("calculation")##the value like a+b split and add
if "+" in expression:## seperating
    a,b =expression.split("+") 
    op="+"
elif "-" in expression:
    a,b = expression.split("-")
    op="-"
elif "*" in expression:
    a,b = expression.split("*")
    op="*"
elif "/" in expression:
    a,b = expression.split("/")
    op="/"
a=float(a)
b=float(b)
match op:
    case "+":
        print(a+b)##applying operators 
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)
    case _:
        print("invalid")


