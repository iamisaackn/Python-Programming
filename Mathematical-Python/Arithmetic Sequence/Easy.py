# ------------------------ EASY -------------------------


'''
Q1).

Calculate the nth term of an arithmetic sequence:
Write a Python function that takes the first term (a1), common difference (d), 
and the term number (n) as input and returns the nth term of the arithmetic sequence.
'''

class MySequence:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def my_calc(self):
        self.b = self.x + (self.z - 1)*self.y
        print(f"The nth term is: {self.b}")


a1 = int(input("Enter the first term: ")) 
d = int(input("Enter the common difference: "))
n = int(input("Enter the term number: "))  

sequence = MySequence( a1, d, n)

sequence.my_calc()


'''
Q2).

Sum of the first n terms in an arithmetic sequence:
Write a Python function that calculates the sum of the first n terms in an arithmetic sequence given the first term (a1),
common difference (d), and the term number (n).
'''

# first term = a1
# common difference = d
# term number = n

def myFunction(a1, d, n):
    return n/2 * (2*(a1)+(n-1)*d)

a1 = int(input("First Term: "))
d = int(input("Common Difference: "))
n = int(input("Term Number: "))

result = myFunction(a1, d, n)
print(f"The sum of the {n} first term is {result}")


"""
Q3)
Check if a given sequence is an arithmetic sequence:
Write a Python function that checks if a given list of numbers forms an arithmetic sequence.
The function should return True if it is an arithmetic sequence and False otherwise.
"""
def isArithmeticSequence():
    pass
    

'''
Q4).

Generate the first n terms of an arithmetic sequence:
Write a Python function that generates the first n terms of an arithmetic sequence 
given the first term (a1), common difference (d), and the term number (n).
'''
# an​=a1​+(n−1)d

# an​ is the nth term,
# a1​ is the first term,
# d is the common difference, and
# n is the term number.

def myFunction(a1, d, n):
    an = [a1+(b-1)*d for b in range(1, n + 1)] # 1 is starting value while (n+1) is ending value
    return an

a1 = int(input("First Term: "))
d = int(input("Common Difference: "))
n = int(input("Term Number: "))

an = myFunction(a1, d, n)

print(f"The answer is {an}")

'''
5. Calculate the average of the terms in an arithmetic sequence:
Write a Python function that calculates the average of the terms in an arithmetic sequence given the first term (a1),
common difference (d), and the term number (n).
'''

# Avarage = a1+((n-1)*d)/2

# --------- Parameters -----------------
# first term (a1)
# common difference (d)
# the term number (n

def myFunction(a1, n, d):
    terms = [a1 + (i - 1) * d for i in range(1, n +1)]
    average = a1 + ((n - 1) * d) / 2
    return terms, average

a1 = int(input("First Term: "))
d = int(input("Common Difference: "))
n = int(input("Term Number: "))

terms, average = myFunction(a1, n, d)

print(f"Terms: {terms} \nAverage: {average}")

'''
Q6).
Create a class for an arithmetic sequence:
Define a Python class ArithmeticSequence that includes methods for 
calculating the nth term, sum of the first n terms, and
checking if a given sequence is an arithmetic sequence.
Use appropriate instance variables.
'''

class ArithmeticSequence:
    def __init__(self, n, a1, d):
        self.n = n
        self.a1 = a1
        self.d = d

    def nTerm(self):
        return self.a1 + (self.n - 1) * self.d
    
    def nSum(self):
        return self.n / 2 * (2 * self.a1 + (self.n - 1) * self.d)
    
    def isArithmeticSequence(self):
        # Check if the difference between consecutive terms is constant
        return all(self.nTerm(i) - self.nTerm(i - 1) == self.d for i in range(2, self.n + 1))

# Get user input
n = int(input("Term Number: "))
d = int(input("Common Difference: "))
a1 = int(input("First Term: "))

# Create an instance of the ArithmeticSequence class
sequence = ArithmeticSequence(n, a1, d)

# Calculate nth term and sum of the first n terms
nTermResults = sequence.nTerm()
nSumResults = sequence.nSum()

# Check if it's an arithmetic sequence
isArithmetic = sequence.isArithmeticSequence()

# Display the results
print(f"nth Term: {nTermResults}\nSum of the first n terms: {nSumResults}")
print(f"Is it an arithmetic sequence? {isArithmetic}")


'''
Q7).
Use lambda function to calculate the nth term:
Write a Python lambda function that takes the first term (a1),
common difference (d), and the term number (n) as arguments 
and returns the nth term of the arithmetic sequence.
'''
nTerm = lambda a1, n, d: a1 + (n + 1) * d

a1 = int(input("First Term: "))
d = int(input("Common Difference: ")) 
n = int(input("Term Number: "))

sequence = nTerm(a1, n, d)
print(f"nth Term: {sequence}")

'''
Q8).
Create a dictionary of arithmetic sequences:
Create a Python dictionary where keys are the names of different arithmetic sequences,
and values are tuples representing the first term, common difference, and term number.
'''

ArithmeticSequence = {}

sequenceName = input("Sequence Name: ")
a1 = int(input("First Term: "))
d = int(input("Common Difference: "))
n = int(input("Term Number: "))

ArithmeticSequence[sequenceName] = (a1, d, n)

sequenceValue = [a1 + (i + 1) * d for i in range(1, n + 1)]

print(f"Arithmetic Sequence: {sequenceValue}")
print(f"Dictionary: {ArithmeticSequence}")

'''
Q9).
Check for odd or even terms:
Write a Python function that takes an arithmetic sequence as a list
and prints whether each term is odd or even. Use a loop and if conditions.
'''

a1 = int(input("First Term: "))
d = int(input("Common Difference: "))
n = int(input("Term Number: "))

sequence = [a1 + (i + 1) * d for i in range(1, n + 1)]
print(f"Arithmetic Sequence: {sequence}")

for term in sequence:  
    if term % 2 !=0:
        print("It is an Odd Number.")
    else:
        print("It is an Even Number.")

'''
Q10).
Concatenate arithmetic sequences:
Write a Python function that takes two arithmetic sequences as lists
and concatenates them into a new arithmetic sequence.
Use lists and a for loop.
'''

A1 = int(input("First list, first term: "))
D = int(input("First list, Common difference: "))
N = int(input("First list, Term Number: "))

a1 = int(input("Second list, first term: "))
d = int(input("Second list, Common difference: "))
n = int(input("Second list, Term Number: "))

firstList = [A1 + (x + 1) * D for x in range(1, N + 1)]
secondList = [a1 + (z + 1) * d for z in range(1, n + 1)]

totalList = firstList
totalList.extend(secondList)
totalList.sort()

print(totalList)