n=int(input("Enter no of elemnts you want to print : "))

list=[0,1,1]

i=0
j=1
l=2

for i in range(0,n-3):
    num=list[i]+list[j]+list[l]
    list.append(num)
    i=i+1
    j=j+1
    l=l+1


print("trifibonacci series = ")

print(list)
