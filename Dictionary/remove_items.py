#The pop() method removes the item wit the specified key name
thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
thisdict.pop("brand")
print(thisdict)

#The 'popitem()' method removes the last inserted item
thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
thisdict.popitem()
print(thisdict)

#The `del` keyword removes the item with the specified key name
thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
del thisdict["brand"]
print(thisdict)

#The `clear()` method empties the dictionary 
thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
thisdict.clear()
print(thisdict)