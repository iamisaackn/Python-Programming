# Change the tuple values
'''
Convert the tuple into a list then covert it back to a tuple
'''
x=("apple", "banana", "cherry")
y= list(x)
y[1]="mango"
x=tuple(y)
print(y)

# Add Items
'''
Since tuples are immutable they lack a built in append() method
'''
'''
1) Convert to a list: convert a tuple into a list then convert it back into a tuple
'''
thistuple=("apple", "banana", "cherry")
y=list(thistuple)
y.append("mango")
thistuple=tuple(y)
print(thistuple)

'''
2) Add a tuple to a tuple: create a tuple with the items the add it to the existing tuple, this is by using the + operator.
'''
thistuple= ("apple", "banana", "cherry")
y=("orange",)
#thistuple=thistuple+y
thistuple+=y
print(thistuple)

# Remove Items
'''
Tuples are unchangeable you convert it into a list remove/ delete then back to a tuple
'''
thistuple=("apple", "banana", "orange")
y=list(thistuple)
# Using remove() function
y.remove("apple")
thistuple=tuple(y)
print(thistuple)

'''You can delete completely using the del keyword'''
thistuple=("apple", "banana", "orange")
del thistuple
print (thistuple)