def check(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
    
n=int(input("Enter the number : "))

print("Given number is : ",check(n))