print("Enter number of elements ")
list=[]
n= int(input("Enter the number of terms : "))

for i in range(0,n):
    num=int(input("Enter the number : "))
    list.append(num)
c=0

for i in range(0,n):
    c=c+1

print("Without using inbuilt function length of list is : ")
print(c)

