list=[]
n= int(input("Enter the number of terms : "))

for i in range(0,n):
    num=int(input("Enter the number : "))
    list.append(num)


print("before replacing list is :")
print(list)


f=list[0] #storing first number in f

l=list[n-1] # storing last numberof list in n

list[0]=l # replacing last element stored in l
list[n-1]=f #replacing first element stored in f

print("after  replacing list is :")
print(list)

