# --------------------------- Fibonacci Sequence ---------------------------

# Write a lambda function to generate the Fibonacci sequence up to the nth term. Use it to find the first 8 terms of the Fibonacci sequence.
Fibonacci = lambda n: n if n<=1 else Fibonacci(n-1) + Fibonacci(n-2)
result = [Fibonacci(i) for i in range(8)]

print(result)

import math

# Assuming Fibonacci is a function that returns the nth Fibonacci number
def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

a = lambda v, w, x, y, z: x if x <= 1 else w * ((Fibonacci(int(math.sqrt(x)) + y) / z) ** v)
b = a(8, 144, 5, 1, 2)

print(b)
