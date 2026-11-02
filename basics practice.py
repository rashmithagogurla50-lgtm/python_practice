a=int(input("enter the number"))##addition
b=int(input("enter the number"))
print(a+b,"add")

n=int(input("power"))##power
print(n**2)

a=int(input("num"))##even or not
if a%2==0:
    print("even")
else:
    print("odd")

a=int(input("num"))##last digit
lastdigit=a%10
print(lastdigit,"last digit")

a=int(input("enter the price"))
if a>=5000:
    discount=a*15/100
elif a>=4000:
    discount=a*10/100
else:
    discount=a*5/100
total=a-discount
print("discount=",discount)
print("total=",total)