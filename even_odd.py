list=[]
n= int(input("Enter the number of terms : "))

for i in range(0,n):
    num=int(input("Enter the number : "))
    list.append(num)


print(" list is :")
print(list)

even=[]
odd=[]

for i in range(0,n):
    if list[i]%2==0:
       even.append(list[i])
    else :
       odd.append(list[i])



print("even numbers are  :")
print(even)
print("odd numbers are  :")
print(odd)



