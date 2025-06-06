############################################
# Python Sets
############################################

#-------------------------------------------
# 1 Create a Set
#-------------------------------------------

thisset = {"one", "two", "three"}
print(thisset)


#-------------------------------------------
# 2 Duplicate values will be ignored
#-------------------------------------------

thisset = {"one", "two", "three", "one"}
print(thisset)

#-------------------------------------------
#3  Get the number of items in a set
#-------------------------------------------

thisset = {"one", "two", "three"}
print(thisset)

#-------------------------------------------
# 4 String, int and boolean data types
#-------------------------------------------

set1 = {"one", "two", "three"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)

#-------------------------------------------
# 5 A set with strings, integers and boolean values
#-------------------------------------------

set1 = {"abc", 34, True, 40, "male"}
print(set1)

#-------------------------------------------
# 6 data type of a set
#-------------------------------------------

myset = {"one", "two", "three"}
print(type(myset))

#-------------------------------------------
# 7 Using the set() constructor to make a set
#-------------------------------------------

thisset = set(("one", "two", "three")) # note the double round-brackets
print(thisset)

############################################
# Access Set Items
############################################

#-------------------------------------------
# 8 Loop through the set, and print the values
#-------------------------------------------

thisset = {"one", "two", "three"}

mylist = ["four", "five"]

thisset.update(mylist)

print(thisset)

############################################
# Remove Set Items
############################################

#-------------------------------------------
# 9 Remove "two" by using the remove() method
#-------------------------------------------

thisset = {"one", "two", "three"}
 
thisset.remove("two")

print(thisset)

#-------------------------------------------
# 10 Remove "two" by using the discard() method
#-------------------------------------------

thisset = {"one", "two", "three"}

thisset.discard("two")

print(thisset)

#-------------------------------------------
# 11 Remove the last item by using the pop() method
#-------------------------------------------

thisset = {"one", "two", "three"}

x = thisset.pop()

print(x)

print(thisset)

#-------------------------------------------
# 12 The clear() method empties the set
#-------------------------------------------

thisset = {"one", "two", "three"}

thisset.clear()

print(thisset)

#-------------------------------------------
# 13 The del keyword will delete the set completely
#-------------------------------------------

thisset = {"one", "two", "three"}
del(thisset)
print(thisset)

############################################
# Join Sets
############################################

#-------------------------------------------
# 14 The union() method returns a new set with all items from both sets
#-------------------------------------------

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#-------------------------------------------
# 15 The update() method inserts the items in set2 into set1
#-------------------------------------------

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
print(len(set1))









