n=int(input("Enter the no of terms you want to find series sum : "))

def factorial(x):
    fact=1
    for i in range(1,x+1):
        fact=fact*i

    return fact

sum=0

for i in range(1,n+1):
    sum=sum+i/factorial(i)

print("Sum of series is : ",sum)