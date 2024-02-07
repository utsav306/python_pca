list=[]
n= int(input("Enter the number of terms : "))

for i in range(0,n):
    num=int(input("Enter the number : "))
    list.append(num)


print("before reversing  list is :")
print(list)


print("after reversing list is : ")

for i in range(n-1,-1,-1):   # here for loop has (n-1 , -1 , -1), it means i will start from n-1 i.e. last index , -1 in between means  i will run from last index to 0 , and last -1 means , i will be decremented by -1
    
    print(list[i],end=" ")

