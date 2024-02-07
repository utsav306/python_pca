srijita=[]

n=int(input("enter the number of terms  : "))

for i in range(0,n):
    x=int(input("Enter yout number :"))
    srijita.append(x)

print("Before swapping")
print(srijita)

a=int(input("Enter the index 1st"))
b=int(input("Enter the index 2nd"))

last=srijita[b]
first=srijita[a]

srijita[a]=last
srijita[b]=first

print("After swappping : ")
print(srijita)
