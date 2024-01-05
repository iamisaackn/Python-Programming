#Using the 'add()' method to add items into a set
thisset={"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#To add a set from another set to the current set use the 'update()' method
thisset = {"apple", "banana", "orange"}
myset = {"blue", "green", "red"}
thisset.update(myset)
print(thisset)

#To add an iterable into a set using 'update()' method
thisset = {"apple", "banana", "cherry"}
thislist = ["green", "blue", "yellow"]
thisdic = {"brand": "Mitsubishi", "color": "yellow"}
thisset.update(thislist, thisdic)
print(thisset)

#To remove an item in a set using 'remove()' method
#If the item to remove doesn't exist it will return an error
thisset={"apple", "banana", "orange"}
thisset.remove("banana")
print(thisset)

#To remove an item in a set using 'discard()' method
#If the item to remove doesn't exist it won't return an error
thisset={"apple", "orange", "banana"}
thisset.discard("apple")
print(thisset)

#To remove an item using 'pop()' method.
#Randomly removes items
thisset={"green", "blue", "yellow"}
thisset.pop()
print(thisset)

#The 'clear()' method empties the set
myset={"apple", "banana", "cherry", "green", "blue", "orange"}
myset.clear()
print(myset)

#The 'del' keyword to delete the set completly
myset={"apple", "banana", "cherry", "green", "blue", "orange"}
del myset #NameError: name 'myset' is not defined
