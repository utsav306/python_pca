n=int(input("Enter no of elemnts you want to print : "))

list=[0,1]

i=0
j=1

for i in range(0,n-2):
    num=list[i]+list[j]
    list.append(num)
    i=i+1
    j=j+1


print("Fibonacci series = ")

print(list)
