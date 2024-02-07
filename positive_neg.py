list=[]
n= int(input("Enter the number of terms : "))

for i in range(0,n):
    num=int(input("Enter the number : "))
    list.append(num)


print(" list is :")
print(list)

pos=[]
neg=[]

for i in range(0,n):
    if list[i]>=0:
       pos.append(list[i])
    else :
       neg.append(list[i])



print("positive numbers are  :")
print(pos)
print("negative numbers are  :")
print(neg)



