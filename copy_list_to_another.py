

list=[]
n= int(input("Enter the number of terms : "))

for i in range(0,n):
    num=int(input("Enter the number : "))
    list.append(num)


print("First list is  :")
print(list)








list2=[] #creating new list

for i in range(0,n):
    list2.append(list[i])  #appending in new list

print("Second list is ")
print(list2)

