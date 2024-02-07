list=[]
n= int(input("Enter the number of terms : "))

for i in range(0,n):
    num=int(input("Enter the number : "))
    list.append(num)

a=int(input("Enter the 1st position you want to swap :"))
b=int(input("Enter the position you want the number to be swapped with  :"))

print("after replacing list is :")
print(list)

f=list[a-1] #storing the  number to be swapped  in f , [a-1] because if user says 2nd position , it implies that 1st index in list ,since it follows 0 based indexing

l=list[b-1] # storing the number to be swapped  in l , [b-1] is done because of same reason;

list[a-1]=l # swapping
list[b-1]=f #swapping

print("after replacing list is :")
print(list)
