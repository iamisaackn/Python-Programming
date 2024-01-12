#-------------------------------- MEDIUM ---------------------------------------

# Create lambda functions to calculate the square and cube of a number. Use them to find the square of 9 and the cube of 4.
square = lambda x: x**2 
cube = lambda y: y **3 

x = square(9)
y = cube(4)

print(x,y)

# Write a lambda function to find the absolute difference between two numbers. Calculate the absolute difference between 15 and 8.
absolute_diff = lambda x,y: abs(x-y)
x = absolute_diff(15,8)

print(x)

# Create a lambda function to calculate the factorial of a number. Use it to find the factorial of 5.
import math

factorial = lambda x: math.factorial(x)
x = factorial(5)

print(x)
# OR
def factorial(x: int):
    return math.factorial(x)

print(factorial(5))

# Define a lambda function to compute the power of a number raised to an exponent. Calculate 2 to the power of 8.
a = lambda x, y: x**y
b = a (2,8)

print(b)

# Write a lambda function to calculate the average of three numbers. Find the average of 12, 18, and 24.
a = lambda x, y, z: (x+y+z)/2
b = a(12, 18, 24)

print(b)