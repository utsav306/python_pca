
import math

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b

def square_root(a):
    return math.sqrt(a)


print("Enter 1 for addition ")
print("Enter 2 for subtraction ")
print("Enter 3 for multiplication ")
print("Enter 4 for division ")
print("Enter 5 for square root ")

n=int(input("Enter your choice : "))

if n==1:
    a=int(input("Enter first number :"))
    b=int(input("Enter second numebr : "))
    ans=add(a,b)
    print("Sum = ",ans)

if n==2:
     a=int(input("Enter first number :"))
     b=int(input("Enter second numebr : "))
     ans=sub(a,b)
     print("subtraction : ",ans)
if n==3:
    a=int(input("Enter first number :"))
    b=int(input("Enter second numebr : "))
    ans=multi(a,b)
    print("multiplication = ",ans)

if n==4:
     a=int(input("Enter first number :"))
     b=int(input("Enter second numebr : "))
     ans=div(a,b)
     print("div : ",ans)

if n==5:
    a=int(input("Enter  number to find sqaure root :"))
    ans=square_root(a)
    print("square root is : ",ans)





