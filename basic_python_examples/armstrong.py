# Check if a number is an Armstrong number without using functions and using user input

num = input("Enter a number: ")
number = int(num)
length = len(num)

total = 0
temp = number

while temp > 0:
    digit = temp % 10
    total += digit ** length
    temp //= 10

if total == number:
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
