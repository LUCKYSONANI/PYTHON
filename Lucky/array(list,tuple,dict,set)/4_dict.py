
############################################
# Python Dictionaries
############################################

#-------------------------------------------
# 1 Create and print a dictionary
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007
}
print(thisdict)

#-------------------------------------------
# 2 Print the "brand" value of the dictionary
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007
}
print(thisdict["brand"])

#-------------------------------------------
# 3 Duplicate values will overwrite existing values
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007,
  "year": 2005
}
print(thisdict)

#-------------------------------------------
# 4 Print the number of items in the dictionary
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007
}
print(len(thisdict))

#-------------------------------------------
# 5 String, int, boolean, and list data types
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",  
  "electric": False,
  "year": 2007,
  "colors": ["red", "white", "blue"]
}

print(thisdict)

############################################
# Access Dictionary Items
############################################

#-------------------------------------------
# 6 Accessing Items
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007
}
x = thisdict["model"]
print(x)

#-------------------------------------------
# 7 Get the value of the "model" key
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007
}
x = thisdict.get("model")
print(x)

#-------------------------------------------
# 8 Get a list of the keys
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007
}

x = thisdict.keys()

print(x)

#-------------------------------------------
# 9 Get a list of the values
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007
}

x = thisdict.values()

print(x)

#-------------------------------------------
# 10 Make a change in the original dictionary, and see that the values list gets updated as well
#-------------------------------------------

car = {
"brand": "Tata",
"model": "Nano",
"year": 2007
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

#-------------------------------------------
# 11 Add a new item to the original dictionary, and see that the values list gets updated as well
#-------------------------------------------

car = {
"brand": "Tata",
"model": "Nano",
"year": 2007
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change

#-------------------------------------------
# 12 Get a list of the key:value pairs
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007
}

x = thisdict.items()

print(x)

#-------------------------------------------
# 13 Check if "model" is present in the dictionary
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007
}

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

############################################
# Change Dictionary Items
############################################

#-------------------------------------------
# 14 Change the "year" to 2018
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007
}

thisdict["year"] = 2018

print(thisdict)

#-------------------------------------------
# 15 Update the "year" of the car by using the update() method
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007
}
thisdict.update({"year": 2020})

print(thisdict)

############################################
# Add Dictionary Items
############################################

#-------------------------------------------
# 16 Adding an item to the dictionary is done by using a new index key and assigning a value to it
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007
}
thisdict["color"] = "red"
print(thisdict)

#-------------------------------------------
# 17 Add a color item to the dictionary by using the update() method
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007
}
thisdict.update({"color": "red"})

print(thisdict)

############################################
# Remove Dictionary Items
############################################

#-------------------------------------------
# 18 The pop() method removes the item with the specified key name
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007
}
thisdict.pop("model")
print(thisdict)

#-------------------------------------------
# 19 The popitem() method removes the last inserted item. 
# (in versions before 3.7, a random item is removed instead)
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007
}
thisdict.popitem()
print(thisdict)

#-------------------------------------------
# 20 The del keyword removes the item with the specified key name
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007
}
del thisdict["model"]
print(thisdict)

#-------------------------------------------
# 21 The del keyword can also delete the dictionary completely
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007
}

print(thisdict) #this will cause an error because "thisdict" no longer exists.

#-------------------------------------------
# 22 The clear() method empties the dictionary
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007
}
thisdict.clear()
print(thisdict)

############################################
# Loop Dictionaries
############################################

#-------------------------------------------
# 23 Print all key names in the dictionary, one by one
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007
}
for x in thisdict:
  print(x)


#-------------------------------------------
# 24 Print all values in the dictionary, one by one
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007
}
for x in thisdict:
  print(thisdict[x])

#-------------------------------------------
# 25 You can also use the values() method to return values of a dictionary
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007
}
for x in thisdict.values():
  print(x)

#-------------------------------------------
# 26 You can use the keys() method to return the keys of a dictionary
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007
}
for x in thisdict.keys():
  print(x)

#-------------------------------------------
# 27 Loop through both keys and values, by using the items() method
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007
}
for x, y in thisdict.items():
  print(x, y)

############################################
# Copy Dictionaries
############################################

#-------------------------------------------
# 28 Make a copy of a dictionary with the copy() method
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007
}
mydict = thisdict.copy()
print(mydict)

#-------------------------------------------
# 29 Make a copy of a dictionary with the dict() function
#-------------------------------------------

thisdict = {
  "brand": "Tata",
  "model": "Nano",
  "year": 2007
}
mydict = dict(thisdict)
print(mydict)

############################################
# Nested Dictionaries
############################################

#-------------------------------------------
# 30 Create a dictionary that contain three dictionaries
#-------------------------------------------

myfamily = {
  "child1" : {
    "name" : "ABC",
    "year" : 2004
  },
  "child2" : {
    "name" : "PQR",
    "year" : 2007
  },
  "child3" : {
    "name" : "XYZ",
    "year" : 2011
  }
}

print(myfamily)

#-------------------------------------------
# 31 Create three dictionaries, then create one dictionary that will contain the other three dictionaries
#-------------------------------------------

myfamily = {
  "child1" : 
  {
    "name" : "ABC",
    "year" : 2004
  },
  "child2" : 
  {
    "name" : "PQR",
    "year" : 2007
  },
  "child3" : 
  {
    "name" : "XYZ",
    "year" : 2011
  }
}

print(myfamily)








