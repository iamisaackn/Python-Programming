# You can access a tuple using numbers in a square bracket
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Negative indexing
'''
Means starting from the end.
-1 is the last number
'''
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#Range of Indexes
'''
Achievable thru specifying where to start and end
Returns the value in a tuple.
'''
thistuple = ("apple", "banana", "cherry")
print(thistuple[1:5])

# START is included while END is not.

#By leaving out the start value, the range will start at the first item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

# By leaving out the end value, the range will go on to the end of the tuple:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# Range of negative indexes
'''
Specify negative indexes if you want to start the search from the end of the tuple:
'''
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# in keyword
'''
To determine if a specified item is present in a tuple use the in keyword:
'''
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
