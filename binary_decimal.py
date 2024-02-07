import math

n=int(input("Enter a binary number : "))
i=0
deci=0
while n!=0:
    r=n%10
    deci=r*math.pow(2,i)+deci
    n=n//10
    i=i+1

print("BInary to decimal =",deci)
