n=int(input("Enter a decimal number : "))
binary=""
while n!=0:
    r=n%2
    binary=str(r)+binary
    n=n//2

print("Decimal to binary = ",binary)