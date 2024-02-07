bachi=[]

n=int(input("enter the number of elemnts "))

for i in range(0,n):
    y=int(input("Enter the elements : "))
    bachi.append(y)

print("list is : ")
print(bachi)

print("after reversing list is ")

for i in range(n-1,-1,-1):
    print(bachi[i],end=" ")


