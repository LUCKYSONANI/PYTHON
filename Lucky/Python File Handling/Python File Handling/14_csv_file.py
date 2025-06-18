
# Example 1: Reading a CSV file
import csv

with open('myfolder/example_1.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

# Example 2: Writing to a CSV file
import csv

data = [
    ["name", "age", "city"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

with open('myfolder/example_2.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)

# Example 3: Appending to a CSV file
import csv

data = ["David", 40, "Houston"]

with open('myfolder/example_1.csv', mode='a', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(data)

# Example 4: Reading specific columns from a CSV file
import csv

with open('myfolder/example_2.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row[0], row[1])  # Print only the product and price columns

# Example 5: Reading a CSV file into a dictionary
import csv

with open('myfolder/example_3.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)

# Example 6: Writing a dictionary to a CSV file
import csv

data = [
    {"id": 1, "first_name": "John", "last_name": "Doe", "email": "john.doe@example.com"},
    {"id": 2, "first_name": "Jane", "last_name": "Smith", "email": "jane.smith@example.com"},
    {"id": 3, "first_name": "Emily", "last_name": "Jones", "email": "emily.jones@example.com"}
]

with open('myfolder/example_4.csv', mode='w', newline='') as file:
    fieldnames = ["id", "first_name", "last_name", "email"]
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerows(data)

# Example 7: Filtering rows in a CSV file
import csv

with open('myfolder/example_2.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if row[0] != "Laptop":  # Filter out rows where product is 'Laptop'
            print(row)

# Example 8: Counting rows in a CSV file
import csv

with open('myfolder/example_3.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    row_count = sum(1 for row in csv_reader)
    print(f'Number of rows: {row_count}')

# Example 9: Modifying a CSV file
import csv

data = []

with open('myfolder/example_1.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if row[0] == "Bob":
            row[1] = 26  # Update Bob's age
        data.append(row)

with open('myfolder/example_1.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)

# Example 10: Reading a large CSV file in chunks
import csv

chunk_size = 2

with open('myfolder/example_3.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    chunk = []
    for row in csv_reader:
        chunk.append(row)
        if len(chunk) == chunk_size:
            print(chunk)
            chunk = []

    if chunk:
        print(chunk)

# Example 11: Creating a CSV file with different delimiters
import csv

data = [
    ["name", "age", "city"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

with open('myfolder/example_5.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file, delimiter=';')
    csv_writer.writerows(data)

# Example 12: Handling CSV files with missing data
import csv

with open('myfolder/example_4.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print([field if field else "N/A" for field in row])  # Replace missing data with 'N/A'

# Example 13: Converting CSV to JSON
import csv
import json

data = []

with open('myfolder/example_3.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data.append(row)

with open('myfolder/example_3.json', mode='w') as file:
    json.dump(data, file, indent=4)

# Example 14: Reading CSV from a URL
import csv
import requests

url = 'https://example.com/example.csv'
response = requests.get(url)
content = response.content.decode('utf-8')
csv_reader = csv.reader(content.splitlines())
for row in csv_reader:
    print(row)

# Example 15: Merging multiple CSV files
import csv

files_to_merge = ['example_1.csv', 'example_2.csv']
merged_data = []

for file_name in files_to_merge:
    with open(file_name, mode='r') as file:
        csv_reader = csv.reader(file)
        merged_data.extend(list(csv_reader))

with open('myfolder/merged.csv', mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(merged_data)