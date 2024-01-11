# Packing is assigning values to a tuple
fruits=("banana", "orange", "mango")

# Unpacking is extracting values back into variables
fruits=("apple", "banana", "cherry")
(green, yellow, red)=fruits
print(green, yellow, red)

'''
The number of variable should much the number of values, if not assign an * asterisk to collect the remaining values as a list
'''
fruits=("apple", "banana", "cherry", "orange", "papaya", "kiwi")
(green, yellow, *red)=fruits
print(green, yellow, red)