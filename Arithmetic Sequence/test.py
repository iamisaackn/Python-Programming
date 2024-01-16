class ArithmeticSequence:
    def __init__(self, n, a1, d):
        self.n = n
        self.a1 = a1
        self.d = d

    def nTerm(self):
        return self.a1 + (self.n - 1) * self.d

    def nSum(self):
        return self.n / 2 * (2 * self.a1 + (self.n - 1) * self.d)

# Get user input
n = int(input("Term Number: "))
d = int(input("Common Difference: "))
a1 = int(input("First Term: "))

# Create an instance of the ArithmeticSequence class
sequence = ArithmeticSequence(n, a1, d)

# Calculate nth term and sum of the first n terms
nTermResult = sequence.nTerm()
nSumResult = sequence.nSum()

# Display the results
print(f"nth Term: {nTermResult}\nSum of the first n terms: {nSumResult}")
