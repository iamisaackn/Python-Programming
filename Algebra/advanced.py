# Problem 1: Quadratic Equation Solver
'''
Solve the quadratic equation ax^2 + bx + c = 0
Use the quadratic formula: x = (-b ± sqrt(b^2 - 4ac)) / (2a)
'''
import math

def quadraticEquation(a, b, c):
    try: 
        value1 = b**2 - 4*a*c

        if value1 < 0:
            print("Error: Rewrite the numbers")

        else: 
            value2 = (-b + math.sqrt(value1)) / (2*a)
            value3 = (-b - math.sqrt(value1)) / (2*a)

            return value2, value3
        
    except Exception as e:
        return str(e)

a = int(input("Insert value of a: "))
b = int(input("Insert value of b: "))
c = int(input("Insert value of c: "))

inputs = quadraticEquation(a, b, c)
print(f"Result: {inputs}")

# Problem: Quadratic Equation Solver

import math

def quadraticEquation(a, b, c):
    try:
        value1 = b**2 - 4*a*c
        if value1 >= 0:
            # If discriminant is non-negative, calculate real solutions
            simple_value1 = (-b + math.sqrt(value1)) / (2*a)
            simple_value2 = (-b - math.sqrt(value1)) / (2*a)
            print(f"Real solutions: {simple_value1}, {simple_value2}")
        else:
            # If discriminant is negative, calculate complex solutions
            complex_value1 = (-b + complex(0, math.sqrt(abs(value1)))) / (2*a)
            complex_value2 = (-b - complex(0, math.sqrt(abs(value1)))) / (2*a)
            print(f"Complex solutions: {complex_value1}, {complex_value2}")

    except Exception as e:
        return str(e)

a = float(input("Enter value \"a\": "))
b = float(input("Enter value \"b\": "))
c = float(input("Enter value \"c\": "))

result = quadraticEquation(a, b, c)


# Problem 2: Matrix Multiplication
'''
Perform matrix multiplication of two matrices
'''

def matrixMultiplication(matrix1, matrix2):
    result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]
    return result

matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]

tMatrix = matrixMultiplication(matrix1, matrix2)
print(f"Answer: {tMatrix}")

# Problem 2: Matrix Multiplication

def matrix_multiplication(matrix1, matrix2):
    return [[sum(a*b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]

matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]

result = matrix_multiplication(matrix1, matrix2)
print(f"Answer: {result}")


# Problem 3: Polynomial Evaluation
'''
Evaluate a polynomial for a given x
Example: 2x^3 + 3x^2 - 4x + 1
'''

# Problem 4: Monte Carlo Integration
'''
Perform Monte Carlo integration to estimate the area under a curve
'''