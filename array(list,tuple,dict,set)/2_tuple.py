#################################
# Create a Tuple
#################################

# -------------------------------
# 1 Create a Tuple
# -------------------------------
mytuple = ("one", "two", "three")
print(mytuple)
# -------------------------------
# 2 Allow Duplicates
# -------------------------------

mytuple = ("one", "two", "three", "one", "three")
print(mytuple)

# -------------------------------
# 3 Tuple Length
# -------------------------------

mytuple = ("one", "two", "three")
print(len(mytuple))  

# -------------------------------
# 4 One item tuple, remember the comma
# -------------------------------

mytuple = ("one",)
print(type(mytuple))

#NOT a tuple
mytuple2 = ("one")
print(type(mytuple2))

# -------------------------------
# 5 Tuple - Data Types
# -------------------------------

tuple1 = ("one", "two", "three")
tuple2 = (1, 3, 5, 2, 4)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

# -------------------------------
# 6 Contain different data types
# -------------------------------

tuple1 = ("xyz", 21, True, 35, "orange")
print(tuple1)

# -------------------------------
# 7 type()
# -------------------------------

mytuple = ("one", "two", "three")
print(type(mytuple))

# -------------------------------
# 8 The tuple() Constructor
# -------------------------------

mytuple = tuple(("one", "two", "three")) # note the double round-brackets
print(mytuple)


#################################
# Access tuple Items
#################################

# -------------------------------
# 9 Print the second item in the tuple
# -------------------------------

mytuple = ("one", "two", "three")
print(mytuple[1])

# -------------------------------
# 10 Print the last item of the tuple:
# -1 refers to the last item, -2 refers to the second last item
# -------------------------------

mytuple = ("one", "two", "three")
print(mytuple[-1])

# -------------------------------
# 11 Return the third, fourth, and fifth item:
# -------------------------------

mytuple = ("one", "two", "three", "four", "five", "six", "seven")
print(mytuple[2,5])

# -------------------------------
# 12 Returns the items from the beginning to 'five', but NOT including, "five":
# -------------------------------

mytuple = ("one", "two", "three", "four", "five", "six", "seven")
print(mytuple[:4])

# -------------------------------
# 13 Returns the items from "three" to the end:
# -------------------------------

mytuple = ("one", "two", "three", "four", "five", "six", "seven")
print(mytuple[2:])

# -------------------------------
# 14 Returns the items from "four" (-4) to, but NOT including "seven" (-1)
# -------------------------------

mytuple = ("one", "two", "three", "four", "five", "six", "seven")
print(mytuple[-4:-1])


# -------------------------------
# 15 Check if Item Exists
# -------------------------------

mytuple = ("one", "two", "three")
if "two" in mytuple:
  print("Yes, 'two' is in the tuple")


#################################
# Update Tuples
#################################

# -------------------------------
# 16 Convert the tuple into a list to be able to change it
# -------------------------------

x = ("one", "two", "three")
y = list(x)
y[1] = "double"
x = tuple(y)

print(x)

# -------------------------------
# 17 Convert the tuple into a list, add "fourth", and convert it back into a tuple
# -------------------------------

mytuple = ("one", "two", "three")
y = list(mytuple)
y.append("fourth")
mytuple = tuple(y)

print(mytuple)

# -------------------------------
# 18 Create a new tuple with the value "fourth", and add that tuple
# -------------------------------

mytuple = ("one", "two", "three")
y = ("fourth",)
mytuple += y

print(mytuple)

# -------------------------------
# 19 Convert the tuple into a list, remove "two", and convert it back into a tuple
# -------------------------------

mytuple = ("one", "two", "three")
y = list(mytuple)
y.remove("two")
mytuple = tuple(y)

print(mytuple)

# -------------------------------
# 20 The del keyword can delete the tuple completely:
# -------------------------------

mytuple = ("one", "two", "three")
del mytuple
print(mytuple) #this will raise an error because the tuple no longer exists


#################################
# Unpack Tuples
#################################

# in Python, we are also allowed to extract the values back into variables. 
# This is called "unpacking":

# -------------------------------
# 21 Unpacking a tuple
# -------------------------------

mytuple = ("one", "two", "three")

(a, b, c) = mytuple

print(a)
print(b)
print(c)

# -------------------------------
# 22 Assign the rest of the values as a list called "red"
# -------------------------------

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# -------------------------------
# 23 Add a list of values the "tropic" variable
# -------------------------------

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)



#################################
# Loop tuple
#################################

# -------------------------------
# 24 Iterate through the items and print the values:
# -------------------------------

mytuple = ("one", "two", "three")
for x in mytuple:
  print(x)

# -------------------------------
# 25 Print all items by referring to their index number
# -------------------------------

mytuple = ("one", "two", "three")
for i in range(len(mytuple)):
  print(mytuple[i])

# -------------------------------
# 26 Print all items, using a while loop to go through all the index numbers
# -------------------------------

mytuple = ("one", "two", "three")
i = 0
while i < len(mytuple):
  print(mytuple[i])
  i = i + 1


#################################
# Join Tuples
#################################

# -------------------------------
# 27 Join two tuples
# -------------------------------

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# -------------------------------
# 28 Multiply the mytuple by 2
# -------------------------------

mytuple = ("one", "two", "three")
mytuple2 = mytuple * 2

print(mytuple2)

# -------------------------------