list = []
n = int(input("Enter the number of terms : "))

for i in range(0, n):
    num = int(input("Enter the number : "))
    list.append(num)

print("Before sorting, the list is:")
print(list)


min=list[0]
max=list[0]

for i in list:
    if i<min:
        min=i
    elif i>max:
        max=i

print(max)
print(min)

