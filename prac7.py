def is_armstrong(num):
    # Function to check if a number is Armstrong
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3  # For Armstrong numbers, use 3 as the power
        temp //= 10
    return num == sum

def armstrong_in_range(start, end):
    # Function to find Armstrong numbers in a given range
    for num in range(start, end + 1):
        if is_armstrong(num):
            print(num)

# Input the range
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

print(f"Armstrong numbers between {start_range} and {end_range}:")
armstrong_in_range(start_range, end_range)