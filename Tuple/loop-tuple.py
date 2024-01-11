#Using for loop
fruits=("apple", "mango", "orange", "banana")
for x in fruits:
    print(x)

# Loop through the ndex
'''
This is by use of len() and range() function to create a suitable iterable, and loop by specifying the index number.
'''
thistuple=("apple", "banana", "orange")
for i in range(len(thistuple)):
    print(thistuple[i])

# Using the while loop
'''
Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.
'''
thistuple=("apple", "banana", "orange")
i=0
while i<len(thistuple):
    print(thistuple[i])
    #i=i+1
    i+=1