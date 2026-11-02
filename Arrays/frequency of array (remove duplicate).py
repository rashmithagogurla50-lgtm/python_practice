arr=[]
n=int(input("how many"))
for i in range(n):
    num=int(input("enter number"))
    arr.append(num)
original=arr.copy()
for i in original:
    if original.count(i)>1:
       arr.remove(i)



print(arr)   
        