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
