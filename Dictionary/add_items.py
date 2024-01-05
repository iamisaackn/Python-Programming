#The 'update()' method will update the dictionary with the items from th given argument
thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
thisdict.update({"year":"1963"})
print(thisdict)

#This is by using a new index key and assingning a value
thisdict={
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
thisdict["color"]="white"
print(thisdict)