# ------------------------ EASY -------------------------
'''
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


x = int(input("Enter the first term: ")) 
y = int(input("Enter the common difference: "))
z = int(input("Enter the term number: "))  

sequence = MySequence( x, y, z)

sequence.my_calc()

