# Demonstrating recursion in Python

# Factorial of a number using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number to find its factorial: "))
print(f"Factorial of {num} is {factorial(num)}")
