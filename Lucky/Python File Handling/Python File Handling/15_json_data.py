
# -----------------------------------------

# Example 1: Writing JSON to a File
import json

data = {
    "name": "John wick",
    "age": 30,
    "city": "New York"
}

with open("example1.json", "w") as file:
    json.dump(data, file)

# -----------------------------------------

# Example 2: Reading JSON from a File
import json

with open("example1.json", "r") as file:
    data = json.load(file)
print(data)

# -----------------------------------------

# Example 3: JSON String to Python Dictionary
import json

json_string = '{"name": "Alice", "age": 25, "city": "London"}'
data = json.loads(json_string)
print(data)

# -----------------------------------------

# Example 4: Python Dictionary to JSON String
import json

data = {
    "name": "Bob",
    "age": 22,
    "city": "Paris"
}
json_string = json.dumps(data)
print(json_string)

# -----------------------------------------

# Example 5: Writing Nested JSON to a File
import json

data = {
    "name": "Emma",
    "age": 28,
    "address": {
        "street": "123 Main St",
        "city": "Los Angeles",
        "state": "CA"
    }
}

with open("example5.json", "w") as file:
    json.dump(data, file)

# -----------------------------------------

# Example 6: Reading Nested JSON from a File
import json

with open("example5.json", "r") as file:
    data = json.load(file)
print(data)

# -----------------------------------------

# Example 7: Handling JSON Arrays
import json

data = [
    {"name": "Tom", "age": 35},
    {"name": "Lucy", "age": 40}
]

with open("example7.json", "w") as file:
    json.dump(data, file)

# -----------------------------------------

# Example 8: Reading JSON Arrays from a File
import json

with open("example7.json", "r") as file:
    data = json.load(file)
print(data)

# -----------------------------------------

# Example 9: Updating JSON Data in a File
import json

with open("example1.json", "r") as file:
    data = json.load(file)

data["age"] = 31

with open("example1.json", "w") as file:
    json.dump(data, file)

# -----------------------------------------

# Example 10: Pretty Printing JSON Data
import json

data = {
    "name": "Olivia",
    "age": 26,
    "city": "Chicago"
}

json_string = json.dumps(data, indent=4)
print(json_string)

# -----------------------------------------

# Example 11: Sorting JSON Keys
import json

data = {
    "city": "Tokyo",
    "name": "Liam",
    "age": 29
}

json_string = json.dumps(data, sort_keys=True)
print(json_string)

# -----------------------------------------

# Example 12: Handling Non-ASCII Characters
import json

data = {
    "name": "Müller",
    "age": 45,
    "city": "Berlin"
}

json_string = json.dumps(data, ensure_ascii=False)
print(json_string)

# -----------------------------------------

# Example 13: Merging Two JSON Objects
import json

data1 = {"name": "Jack", "age": 32}
data2 = {"city": "Sydney", "country": "Australia"}

merged_data = {**data1, **data2}
print(json.dumps(merged_data))

# -----------------------------------------

# Example 14: Filtering JSON Data
import json

data = [
    {"name": "Sam", "age": 30},
    {"name": "Pam", "age": 22}
]

filtered_data = [person for person in data if person["age"] > 25]
print(json.dumps(filtered_data, indent=4))

# -----------------------------------------

# Example 15: Creating JSON from User Input
import json

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

data = {
    "name": name,
    "age": age,
    "city": city
}

with open("example15.json", "w") as file:
    json.dump(data, file)
