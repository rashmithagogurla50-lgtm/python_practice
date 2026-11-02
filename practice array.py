arr=[1,2,3]##indiv num
print(arr[1])

arr=[1,2,3,4]##adding numbers
arr.append(5)
print(arr)

arr=[1,2,3,4]##replace
arr[2]=10
print(arr)

arr=[1,2,3,4]##dlt method one
arr.pop()
print(arr)

arr=[1,2,3,4]##method 2(index)
arr.pop(2)
print(arr)

arr=[1,2,3,4]##method 3(num)
arr.remove(4)
print(arr)


n=int(input("how many"))#swaping array method 1
arr=[]
for i in range(n):
    num=int(input("num"))
    arr.append(num)
print("before swap",arr)
arr[0],arr[n-1]=arr[n-1],arr[0]
print("after",arr)

n=int(input("how many"))#swaping using mid
arr=[]
i=0
for i in range(n):
    num=int(input("num"))
    arr.append(num)
mid=len(arr)//2
i=0
while i<mid:
    arr[i],arr[len(arr)-i-1]=arr[len(arr)-i-1],arr[i]
    i=i+1
print(arr)

n=int(input("how many"))##minimum value 
arr=[]
for i in range(n):
    num=int(input("num"))
    arr.append(num)
minimum=arr[0]
for i in arr:
    if i<minimum:
     minimum=i
print(minimum,"minimum")

n=int(input("how many"))##maximum value
arr=[]
for i in range(n):
    num=int(input("num"))
    arr.append(num)
max=arr[0]
for i in arr:
    if i>max:
      max=i
print(max,"max")

n=int(input("how many"))##sum
arr=[]
for i in range(n):
   num=int(input("num"))
   arr.append(num)
total=0
for i in arr:
   total=total+i
print("total",total)

n=int(input("how many"))##second largest number
arr=[]
for i in range(n):
   num=int(input("num"))
   arr.append(num)
arr.sort()
print("second largest num",arr[-2])