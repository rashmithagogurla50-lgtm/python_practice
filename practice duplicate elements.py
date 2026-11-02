n=int(input("how many"))##duplicate
arr=[]
for i in range(n):
    num=int(input("num"))
    arr.append(num)
duplicate=[]
for i in arr:
    if arr.count(i)>1 and i not in duplicate:
     duplicate.append(i)
print("duplicate",duplicate)

n=int(input("how many"))##count of duplicate
arr=[]
for i in range(n):
   num=int(input("num"))
   arr.append(num)
duplicate=[]
for i in arr:
    if arr.count(i)>1 and i not in duplicate:
       duplicate.append(i)
print("duplicate",duplicate)
print(len(duplicate))

n=int(input("how many"))##output numbers which are not repeated
arr=[]
for i in range(n):
   num=int(input("num"))
   arr.append(num)
unique =[]
for i in arr:
   if arr.count(i)==1:
      unique.append(i)
print("not repeated",unique)

n=int(input("how many"))##removing duplicate
arr=[]
for i in range(n):
   num=int(input("num"))
   arr.append(num)
unique=[]
for i in arr:
   if i not in unique:
      unique.append(i)
print(arr,"original list")
print(unique,"after removing duplicate")

arr1=[]##common in 2 arrays
arr2=[]
n=int(input("how many"))
for i in range(n):
   num=int(input("num"))
   arr1.append(num)
m=int(input("how many"))
for i in range(m):
   num=int(input("num"))
   arr2.append(num)
common=[]
for i in arr1:
   if arr2.count(i)and i not in common:
      common.append(i)
print(common,"common")

arr1=[]
arr2=[]
n=int(input("how many"))
for i in range(n):
   num=int(input("num"))
   arr1.append(num)
m=int(input("how many"))
for i in range(m):
   num=int(input("num"))
   arr2.append(num)
common=[]
for i in arr1:
   if arr2.count(i) and i not in common:
      common.append(i)
print(common,"common")
duplicate=[]
for i in arr:
   if arr1.count(i)>1 and arr2.count(i)>1 and i not in duplicate:
      duplicate.append(i)
print(duplicate)