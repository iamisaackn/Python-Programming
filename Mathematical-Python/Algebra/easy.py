
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

# Problem 5: Sum of Even Numbers
'''
Find the sum of even numbers from 1 to n
Equation: 2 + 4 + 6 + ... + n
'''

def mySolution(n):
    return sum(i for i in range(2, n + 1, 2))

n = int(input("Term Number: "))

result = mySolution(n)
print(f"Answer: {result}")

# Problem 6: Word Reversal
'''
Reverse a given word
Example: "Python" => "nohtyP"
''' 

def wordReversal(word):
    return word[::-1] 

word = "Python"
result = wordReversal(word)

print(f"Answer: {result}")  
    
# Problem 6: Unique Elements in a List
'''
Find the unique elements in a list
Example: [1, 2, 3, 2, 4, 5, 3] => [1, 2, 3, 4, 5]
'''
def uniqueElements(newList):
    return list(set(newList))

mylist = [1, 2, 3, 2, 4, 5, 3]

result = uniqueElements(mylist)
print(f"Answer: {result}")

# Problem 7: File Handling - Find Average
'''
Read numbers from a file, calculate the average, 
and write it to another file
'''
def calculate_average(filename):
    try:
        with open(filename, 'r') as file:
            numbers = [int(line.strip()) for line in file]
            average = sum(numbers) / len(numbers)
            
        with open('average_result.txt', 'w') as result_file:
            result_file.write(f"Average: {average}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Assume there is a file named 'numbers.txt' with numbers on each line
calculate_average('numbers.txt')
print("Problem 4: Average calculated and written to 'average_result.txt'")

