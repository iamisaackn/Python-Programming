
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