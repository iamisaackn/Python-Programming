
# Problem 1: Solve for x
'''
Equation: 2x + 5 = 13
Solve for x
'''

x = (13 - 5) / 5

print(f"Anser: {x}")

# Problem 2: Sum of Squares
'''
Find the sum of squares of numbers from 1 to n
Equation: 1^2 + 2^2 + 3^2 + ... + n^2
'''
def sum_of_squares(n):
    result = sum(i**2 for i in range(1, n+1))
    return result

n_value = 4
result = sum_of_squares(n_value)
print(f"Problem 2: The sum of squares from 1 to {n_value} is {result}")

# Problem 3: Area of a Rectangle
'''
Calculate the area of a rectangle
Equation: Area = length * width
'''
def calculate_rectangle_area(length, width):
    area = length * width
    return area

length_value = 5
width_value = 8
result = calculate_rectangle_area(length_value, width_value)
print(f"Problem 3: The area of the rectangle is {result}")

# Problem 4: Factorial using Recursion
'''
Calculate the factorial of a number using recursion
Equation: n! = n * (n-1) * (n-2) * ... * 1
'''

