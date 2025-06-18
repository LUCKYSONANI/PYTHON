
# Example 1: Reading a JSON file
import json

with open('myfolder/example1.json', 'r') as file:
    data = json.load(file)
print(data)

# -------------------------------

# Example 2: Writing to a JSON file
import json

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

with open('myfolder/example2.json', 'w') as file:
    json.dump(data, file)

# -------------------------------

# Example 3: Pretty Printing JSON data
import json

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

with open('myfolder/example3.json', 'w') as file:
    json.dump(data, file, indent=4)

# -------------------------------

# Example 4: Reading JSON data from a URL
import json
import urllib.request

url = 'https://jsonplaceholder.typicode.com/posts'
response = urllib.request.urlopen(url)
data = json.loads(response.read().decode())
print(data)

# -------------------------------

# Example 5: Handling JSON decode error
import json

json_string = '{"name": "John Doe", "age": 30, "city": "New York"'

try:
    data = json.loads(json_string)
except json.JSONDecodeError as e:
    print(f"JSON decode error: {e}")

# -------------------------------

# Example 6: Writing JSON data to a string
import json

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

json_string = json.dumps(data)
print(json_string)

# -------------------------------

# Example 7: Reading JSON data from a string
import json

json_string = '{"name": "John Doe", "age": 30, "city": "New York"}'
data = json.loads(json_string)
print(data)

# -------------------------------

# Example 8: Updating JSON data in a file
import json

with open('myfolder/example8.json', 'r+') as file:
    data = json.load(file)
    data['age'] = 31
    file.seek(0)
    json.dump(data, file)
    file.truncate()

# -------------------------------

# Example 9: Merging two JSON objects
import json

data1 = {
    "name": "John Doe",
    "age": 30
}

data2 = {
    "city": "New York",
    "occupation": "Software Developer"
}

merged_data = {**data1, **data2}

with open('myfolder/example9.json', 'w') as file:
    json.dump(merged_data, file)

# -------------------------------

# Example 10: Reading nested JSON data
import json

with open('myfolder/example10.json', 'r') as file:
    data = json.load(file)
print(data['address']['city'])

# -------------------------------

# Example 11: Writing nested JSON data
import json

data = {
    "name": "John Doe",
    "age": 30,
    "address": {
        "city": "New York",
        "zip": "10001"
    }
}

with open('myfolder/example11.json', 'w') as file:
    json.dump(data, file)

# -------------------------------

# Example 12: Converting JSON data to a Python object
import json

json_string = '{"name": "John Doe", "age": 30, "city": "New York"}'
data = json.loads(json_string)

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

person = Person(**data)
print(person.__dict__)

# -------------------------------

# Example 13: Converting a Python object to JSON data
import json

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

person = Person("John Doe", 30, "New York")
json_data = json.dumps(person.__dict__)
print(json_data)

# -------------------------------

# Example 14: Reading JSON data with datetime objects
import json
from datetime import datetime

def datetime_parser(dct):
    for key, value in dct.items():
        if isinstance(value, str) and 'T' in value:
            try:
                dct[key] = datetime.fromisoformat(value)
            except ValueError:
                pass
    return dct

with open('myfolder/example14.json', 'r') as file:
    data = json.load(file, object_hook=datetime_parser)
print(data)

# -------------------------------

# Example 15: Writing JSON data with datetime objects
import json
from datetime import datetime

data = {
    "name": "John Doe",
    "timestamp": datetime.now().isoformat()
}

with open('myfolder/example15.json', 'w') as file:
    json.dump(data, file)

