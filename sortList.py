list = []
n = int(input("Enter the number of terms : "))

for i in range(0, n):
    num = int(input("Enter the number : "))
    list.append(num)

print("Before sorting, the list is:")
print(list)

for i in range(n - 1):
    min_index = i
    for j in range(i + 1, n):
        if list[j] < list[min_index]:
            min_index = j

    # Swap the found minimum element with the current element
    list[i], list[min_index] = list[min_index], list[i]  #ek line swap ho jata python me
    

print("After sorting, the list is:")
print(list)


list.sort()


