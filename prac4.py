teddy=[]

n= int(input("enter the no of elements "))

for i in range(0,n):
    a=int((input("enter the numbers : ")))
    teddy.append(a)

print("The list is ")
print(teddy)

for i in range(0,n-1):
    min=i
    for j in range(i+1,n):
        if teddy[j]<teddy[min]:
            min=j

    teddy[min],teddy[i]=teddy[i],teddy[min]

print("minimum element = ",teddy[0])
print("max element : ",teddy[n-1])

print("2nd lar =",teddy[n-2])