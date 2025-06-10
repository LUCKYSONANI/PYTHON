#################################
# Create List
#################################

# -------------------------------
# 1 Create a List:
# -------------------------------
mylist = ["one", "two", "three"]
print(mylist)

# -------------------------------
# 2 Allow Duplicates
# -------------------------------

mylist = ["one", "two", "three", "one", "three"]
print(mylist)

# -------------------------------
# 3 List Length
# -------------------------------

mylist = ["one", "two", "three"]
print(len(mylist))  

# -------------------------------
# 4 List Items - Data Types
# -------------------------------

list1 = ["one", "two", "three"]
list2 = [1, 3, 5, 2, 4]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

# -------------------------------
# 5 Contain different data types
# -------------------------------

list1 = ["xyz", 21, True, 35, "orange"]
print(list1)

# -------------------------------
# 6 type()
# -------------------------------

mylist = ["one", "two", "three"]
print(type(mylist))

# -------------------------------
# 7 The list() Constructor
# -------------------------------

mylist = list(("one", "two", "three"))
print(mylist)


#################################
# Access List Items
#################################

# -------------------------------
# 8 Print the second item of the list
# -------------------------------

mylist = ["one", "two", "three"]
print(mylist[1])

# -------------------------------
# 9) Print the last item of the list: 
# -1 refers to the last item, -2 refers to the second last item
# -------------------------------

mylist = ["one", "two", "three"]
print(mylist[-1])

# -------------------------------
# 10 Return the third, fourth, and fifth item:
# -------------------------------

mylist = ["one", "two", "three", "four", "five", "six", "seven"]
print(mylist[2:5])

# -------------------------------
# 11 Returns the items from the beginning to, but NOT including, "five":
# -------------------------------

mylist = ["one", "two", "three", "four", "five", "six", "seven"]
print(mylist[:4])

# -------------------------------
# 12 Returns the items from "three" to the end:
# -------------------------------

mylist = ["one", "two", "three", "four", "five", "six", "seven"]
print(mylist[2:])

# -------------------------------
# 13 Returns the items from "four" (-4) to, but NOT including "seven" (-1)
# -------------------------------

mylist = ["one", "two", "three", "four", "five", "six", "seven"]
print(mylist[-4:-1])


# -------------------------------
# 14 Check if Item Exists
# -------------------------------

mylist = ["one", "two", "three"]

if "two" in mylist:
  print("Yes, 'two' is in the list")

#################################
#  Change List Items
#################################

# -------------------------------
# 15 Change the second item
# -------------------------------

mylist = ["one", "two", "three"]
mylist[1] = "double"

print(mylist)

# -------------------------------
# 16 Change the values "two" and "three" with the values "double" and "triple"
# -------------------------------

mylist = ["one", "two", "three", "four", "five", "six", "seven"]
mylist[1:3] = ["double", "triple"]

print(mylist)

# -------------------------------
# 17 Change the second value by replacing it with two new values
# -------------------------------

mylist = ["one", "two", "three"]
mylist[1:2] = ["double", "triple"]

print(mylist)


# -------------------------------
# 18 Change the second and third value by replacing it with one value
# -------------------------------

mylist = ["one", "two", "three"]
mylist[1:3] = ["double"]

print(mylist)


#################################
#  Add List Items
#################################

# -------------------------------
# 19 Using the append() method to append an item
# -------------------------------

mylist = ["one", "two", "three"]
mylist.append("fourth")

print(mylist)

# -------------------------------
# 20 Insert "triple" as the third item:
# -------------------------------

mylist = ["one", "two", "three"]
mylist.insert(2, "triple")

print(mylist)

# -------------------------------
# 21 Add the elements of list2 to list1
# -------------------------------

list1 = ["one", "two", "three"]
list2 = ["four", "five", "six"]
list1.extend(list2)
print(list1)

#################################
# Remove List Items
#################################

# -------------------------------
# 22 Remove Specified Item
# -------------------------------

mylist = ["one", "two", "three"]
mylist.remove("two")

print(mylist)

# -------------------------------
# 23 Remove Specified Index
# -------------------------------

mylist = ["one", "two", "three"]
mylist.pop(1)

print(mylist)

# -------------------------------
# 24 Remove the last item:
# -------------------------------

mylist = ["one", "two", "three"]
mylist.pop()

print(mylist)

# -------------------------------
# 25 The del keyword also removes the specified index
# -------------------------------

mylist = ["one", "two", "three"]
del mylist[1]

print(mylist)

# -------------------------------
# 26 Delete the entire list
# -------------------------------

mylist = ["one", "two", "three"]
del mylist

# -------------------------------
# 27 Clear the list content
# -------------------------------

mylist = ["one", "two", "three"]
mylist.clear()

print(mylist)


#################################
#  Loop Lists
#################################

# -------------------------------
# 28 Print all items in the list, one by one
# -------------------------------

mylist = ["one", "two", "three"]

for x in mylist:
  print(x)

# -------------------------------
# 29 Print all items by referring to their index number
# -------------------------------

mylist = ["one", "two", "three"]

for i in range(len(mylist)):
  print(mylist[i])

# -------------------------------
# 30 Print all items, using a while loop to go through all the index numbers
# -------------------------------

mylist = ["one", "two", "three"]
i = 0

while i < len(mylist):
  print(mylist[i])
  i = i + 1

# -------------------------------
# 31 A short hand for loop that will print all items in a list:
# -------------------------------

mylist = ["one", "two", "three"]
[print(x) for x in mylist]


#################################
# Sort Lists
#################################

# -------------------------------
# 32 Sort the list alphabetically
# -------------------------------

mylist = ["gujarat", "bihar", "maharastra", "delhi", "manipur"]
mylist.sort()
print(mylist)

# -------------------------------
# 33 Sort the list numerically
# -------------------------------

mylist = [100, 50, 65, 82, 23]
mylist.sort()
print(mylist)

# -------------------------------
# 34 Sort the list descending
# -------------------------------

mylist = ["gujarat", "bihar", "maharastra", "delhi", "manipur"]
mylist.sort(reverse = True)
print(mylist)

# -------------------------------
# 35 Reverse the order of the list items
# -------------------------------

mylist = ["gujarat", "bihar", "maharastra", "delhi", "manipur"]
mylist.reverse()
print(mylist)


#################################
# Copy Lists
#################################

# -------------------------------
# 36 Make a copy of a list with the copy() method
# -------------------------------

mylist = ["one", "two", "three"]
newlist = mylist.copy()
print(newlist)

# -------------------------------
# 37 Make a copy of a list with the list() method
# -------------------------------

mylist = ["one", "two", "three"]
newlist = list(mylist)
print(newlist)


#################################
# Join Lists
#################################

# -------------------------------
# 38 Join two list
# -------------------------------

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# -------------------------------
# 39 Append list2 into list1
# -------------------------------


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# -------------------------------
# 40 Use the extend() method to add list2 at the end of list1
# -------------------------------

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# -------------------------------
# 
# -------------------------------