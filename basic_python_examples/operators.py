# Demonstrating different types of operators in Python

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

# Arithmetic Operators
print("Arithmetic Operators:")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a ** b =", a ** b)
print("a // b =", a // b)

# Comparison Operators
print("\nComparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Logical Operators
print("\nLogical Operators:")
print("a > 5 and b < 5:", a > 5 and b < 5)
print("a > 5 or b > 5:", a > 5 or b > 5)
print("not(a > 5):", not(a > 5))

# Assignment Operators
print("\nAssignment Operators:")
c = a
print("c =", c)
c += b
print("c += b:", c)
c *= b
print("c *= b:", c)

# Bitwise Operators
print("\nBitwise Operators:")
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("~a:", ~a)
print("a << 1:", a << 1)
print("a >> 1:", a >> 1)
