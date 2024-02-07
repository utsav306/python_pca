n=int(input("Enter number of elements : "))

list=[]
for i in range(0,n):
    x=int(input())
    list.append(x)

print("Before sort : ",list)

for i in range(n-1):
    min=i
    for j in range(i+1,n):
        if list[j]<list[min]:
            min=j
    list[i],list[min]=list[min],list[i]




print("After sorting : ")
print(list)