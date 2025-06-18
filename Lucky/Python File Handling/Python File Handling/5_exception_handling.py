# Example 1: Reading the entire content of a file
try:
    with open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error reading the file.")

# Example 2: Reading the file line by line using a loop
try:
    with open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r') as file:
        for line in file:
            print(line, end='')
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error reading the file.")

# Example 3: Reading the file using readline()
try:
    with open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r') as file:
        line = file.readline()
        while line:
            print(line, end='')
            line = file.readline()
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error reading the file.")

# Example 4: Writing to a file (overwriting existing content)
try:
    with open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'w') as file:
        file.write("New content replacing the old content.")
except IOError:
    print("Error writing to the file.")

# Example 5: Appending to a file
try:
    with open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'a') as file:
        file.write("\nThis line is appended to the file.")
except IOError:
    print("Error writing to the file.")

# Example 6: Using 'with' statement to handle files
try:
    with open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error reading the file.")

# Example 7: Using tell() and seek() methods
try:
    with open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r') as file:
        print("Current position:", file.tell())
        print("Reading first 5 characters:", file.read(5))
        print("Current position:", file.tell())
        file.seek(0)
        print("Position reset to the beginning:", file.tell())
        print("Reading again:", file.read(5))
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error reading the file.")

# Example 8: Handling file not found exception
try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error reading the file.")

# Example 9: Handling generic I/O exceptions
try:
    with open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r') as file:
        content = file.read()
        print(content)
except IOError as e:
    print(f"An IOError occurred: {e}")

# Example 10: Writing multiple lines to a file
lines_to_write = [
    "Line 1\n",
    "Line 2\n",
    "Line 3\n"
]
try:
    with open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'w') as file:
        file.writelines(lines_to_write)
except IOError:
    print("Error writing to the file.")
