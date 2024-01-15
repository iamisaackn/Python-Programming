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

'''
Q4).

Generate the first n terms of an arithmetic sequence:
Write a Python function that generates the first n terms of an arithmetic sequence 
given the first term (a1), common difference (d), and the term number (n).
'''

def myFunction():