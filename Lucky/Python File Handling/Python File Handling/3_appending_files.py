
# Example 1: Appending a single line to a file
with open('myfolder/test.txt', 'a') as file:
    file.write('This is an appended line.\n')

# Example 2: Appending multiple lines to a file
lines_to_append = ['This is the second appended line.\n', 'This is the third appended line.\n']
with open('myfolder/test.txt', 'a') as file:
    file.writelines(lines_to_append)

# Example 3: Appending a line using a variable
line_to_append = 'This is a line appended using a variable.\n'
with open('lucky/PYTHON/Lucky/Python file handling/myfolder/test.txt', 'a') as file:
    file.write(line_to_append)

# Example 4: Appending with a loop
for i in range(1, 4):
    with open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'a') as file:
        file.write(f'This is appended line {i} in a loop.\n')

# Example 5: Appending user input to a file
user_input = 'This is a user input line.\n'
with open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'a') as file:
    file.write(user_input)

# Example 6: Appending formatted string to a file
name = 'John'
age = 30
with open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'a') as file:
    file.write(f'Name: {name}, Age: {age}\n')

# Example 7: Appending content conditionally
condition = True
if condition:
    with open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'a') as file:
        file.write('Conditionally appended line.\n')

# Example 8: Appending from another file
with open('source.txt', 'r') as source_file:
    content = source_file.read()
with open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'a') as target_file:
    target_file.write(content)

# Example 9: Appending a dictionary's content to a file
data = {'key1': 'value1', 'key2': 'value2'}
with open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'a') as file:
    for key, value in data.items():
        file.write(f'{key}: {value}\n')

# Example 10: Appending a list's content to a file
list_data = ['item1', 'item2', 'item3']
with open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'a') as file:
    for item in list_data:
        file.write(f'{item}\n')
