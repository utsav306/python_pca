list=[]
n= int(input("Enter the number of terms : "))

for i in range(0,n):
    num=int(input("Enter the number : "))
    list.append(num)


print("list is :")
print(list)

ele=int(input("Enter the number you want check is present or  not : "))

c=0 #initialising count variable i.e c with 0

for i in range(0,n):
    if(list[i]==ele):
        c=c+1 #incrementing c when we encounter the element

if(c>0):
    print("element present ")
else:
    print("elemnt not present ")
