srijita_love=[]

n=int(input("Enter no of elements "))

for i in range(0,n):
    x=int(input("Enter the numbers : "))
    srijita_love.append(x)

print("your list is : ")
print(srijita_love)

for i in range(0,n-1):
    min_index=i
    for j in range(i+1,n):
        if srijita_love[j]<srijita_love[min_index]:
            min_index=j

    srijita_love[min_index],srijita_love[i]=srijita_love[i],srijita_love[min_index]




print("After sorting ")

print(srijita_love)


