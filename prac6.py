my_love=[]

n=int(input("Enter number of elemnents "))

for i in range(0,n):
    x=int(input("Enter element :"))
    my_love.append(x)

print("before sorting : ")
print(my_love)

my_love.sort()

print(my_love)