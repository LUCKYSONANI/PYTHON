
# 'r' is used open file in reading mode

# Example 1: Opening and Closing a File
with open('myfolder/test.txt', 'r') as file:
    pass  # File is opened and immediately closed when using 'with' statement

# Example 2: Reading the Entire File using read()
with open('myfolder/test.txt', 'r') as file:
    content = file.read()
    print(content)

# Example 3: Reading Line by Line using readline()
with open('myfolder/test.txt', 'r') as file:
    line1 = file.readline()
    print(line1)

# Example 4: Reading All Lines using readlines()
with open('myfolder/test.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

# Example 5: Reading File with Explicit Close
file = open('myfolder/test.txt', 'r')
content = file.read()
print(content)
file.close()

# Example 6: Reading Specific Number of Characters
with open('myfolder/test.txt', 'r') as file:
    content = file.read(10)
    print(content)

# Example 7: Reading Line by Line in a Loop
with open('myfolder/test.txt', 'r') as file:
    for line in file:
        print(line, end='')

# Example 8: Reading First Line
with open('myfolder/test.txt', 'r') as file:
    first_line = file.readline()
    print(first_line)

# Example 9: Reading Second Line
with open('myfolder/test.txt', 'r') as file:
    file.readline()  # Skip first line
    second_line = file.readline()
    print(second_line)

# Example 10: Reading File Using File Object as Iterator
with open('myfolder/test.txt', 'r') as file:
    for line in file:
        print(line, end='')

# Example 11: Reading File Using seek() and read()
with open('myfolder/test.txt', 'r') as file:
    file.seek(0)
    content = file.read()
    print(content)

# Example 12: Reading File Using seek() to Start
with open('myfolder/test.txt', 'r') as file:
    file.seek(0)
    line = file.readline()
    print(line)

# Example 13: Reading File Using seek() to Specific Position
with open('myfolder/test.txt', 'r') as file:
    file.seek(10)
    content = file.read()
    print(content)

# Example 14: Reading File to a List
with open('myfolder/test.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')

# Example 15: Checking if File is Closed
file = open('myfolder/test.txt', 'r')
print(file.closed)
file.close()
print(file.closed)

# Example 16: Using Context Manager to Ensure File is Closed
with open('myfolder/test.txt', 'r') as file:
    content = file.read()
print(file.closed)

# Example 17: Reading File with Exception Handling
try:
    with open('myfolder/test.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")

# Example 18: Reading File in Binary Mode
with open('myfolder/test.txt', 'rb') as file:
    content = file.read()
    print(content)

# Example 19: Reading File Using readlines() with Loop
with open('myfolder/test.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')

# Example 20: Reading File Using Different Buffer Sizes
with open('myfolder/test.txt', 'r') as file:
    while True:
        buffer = file.read(10)
        if not buffer:
            break
        print(buffer, end='')
