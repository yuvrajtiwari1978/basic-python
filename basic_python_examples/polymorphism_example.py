# Demonstrating polymorphism, method overriding, arbitrary arguments, method overloading (simulated), and super() in Python

# Polymorphism and Method Overriding
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")

# Method Overloading (simulated using default arguments)
class MathOperations:
    def add(self, a, b, c=None):
        if c is not None:
            print("Sum of three numbers:", a + b + c)
        else:
            print("Sum of two numbers:", a + b)

# Using super()
class Base:
    def __init__(self):
        print("Base class constructor")

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Derived class constructor")

# Arbitrary arguments
def arbitrary_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# Testing polymorphism and method overriding
p = Parent()
c = Child()
p.greet()
c.greet()

# Testing method overloading simulation
math_op = MathOperations()
math_op.add(1, 2)
math_op.add(1, 2, 3)

# Testing super()
d = Derived()

# Testing arbitrary arguments
arbitrary_args(1, 2, 3, name="Alice", age=30)
