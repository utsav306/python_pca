n=int(input("Enter the number : "))

copy=n
sum=0

while n!=0:
    r=n%10
    sum=sum+r*r*r
    n=n//10


if sum==copy:
    print("armstrong")
else:
    print("not armstrong ")