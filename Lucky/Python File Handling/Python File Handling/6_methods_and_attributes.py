
# Example 1: Checking file name attribute
file = open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r')
print(f'File name: {file.name}')
file.close()

# Example 2: Checking file mode attribute
file = open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r')
print(f'File mode: {file.mode}')
file.close()

# Example 3: Checking if file is closed
file = open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r')
file.close()
print(f'Is file closed? {file.closed}')

# Example 4: Using with statement to open file
with open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r') as file:
    content = file.read()
    print(content)

# Example 5: Using with statement to ensure file is closed
with open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r') as file:
    content = file.read()
print(f'Is file closed? {file.closed}')

# Example 6: Using tell() to get current file position
file = open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r')
print(f'Current file position: {file.tell()}')
file.close()

# Example 7: Using seek() to change file position
file = open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r')
file.seek(10)
print(f'New file position: {file.tell()}')
file.close()

# Example 8: Reading from a new file position
file = open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r')
file.seek(10)
content = file.read()
print(content)
file.close()

# Example 9: Using seek() and tell() together
file = open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r')
file.seek(5)
print(f'Current file position: {file.tell()}')
content = file.read()
print(content)
file.close()

# Example 10: Truncating file to 10 bytes
file = open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r+')
file.truncate(10)
file.close()

# Example 11: Verifying file truncation
file = open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r')
content = file.read()
print(content)
file.close()

# Example 12: Opening file in append mode and checking attributes
file = open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'a')
print(f'File name: {file.name}')
print(f'File mode: {file.mode}')
print(f'Is file closed? {file.closed}')
file.close()

# Example 13: Opening file in write mode and checking attributes
file = open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'w')
print(f'File name: {file.name}')
print(f'File mode: {file.mode}')
print(f'Is file closed? {file.closed}')
file.close()

# Example 14: Using with statement to write to file
with open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'w') as file:
    file.write('This is a new line.')
print(f'Is file closed? {file.closed}')

# Example 15: Using seek() to move to end of file
file = open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r')
file.seek(0, 2)
print(f'File position at end: {file.tell()}')
file.close()

# Example 16: Using tell() after reading part of the file
file = open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r')
file.read(5)
print(f'Current file position: {file.tell()}')
file.close()

# Example 17: Using seek() with negative offset
file = open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r')
file.seek(-5, 2)
print(f'New file position: {file.tell()}')
file.close()

# Example 18: Truncating file to 5 bytes
file = open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r+')
file.truncate(5)
file.close()

# Example 19: Verifying file truncation to 5 bytes
file = open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r')
content = file.read()
print(content)
file.close()

# Example 20: Using with statement for binary file operations
with open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'rb') as file:
    content = file.read()
    print(content)

# Example 21: Using tell() in binary mode
file = open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'rb')
print(f'Current file position: {file.tell()}')
file.close()

# Example 22: Using seek() in binary mode
file = open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'rb')
file.seek(5)
print(f'New file position: {file.tell()}')
file.close()

# Example 23: Using seek() to go to beginning of file
file = open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r')
file.seek(0)
print(f'Current file position: {file.tell()}')
file.close()

# Example 24: Using seek() to skip first line
file = open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r')
file.readline()
file.seek(file.tell())
content = file.read()
print(content)
file.close()

# Example 25: Using tell() to get position after readline()
file = open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r')
file.readline()
print(f'Current file position: {file.tell()}')
file.close()

# Example 26: Using seek() with a large file
file = open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r')
file.seek(100)
print(f'New file position: {file.tell()}')
file.close()

# Example 27: Truncating file completely
file = open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r+')
file.truncate(0)
file.close()

# Example 28: Verifying complete truncation
file = open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r')
content = file.read()
print(content)
file.close()

# Example 29: Using with statement for file truncation
with open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r+') as file:
    file.truncate(10)
print(f'Is file closed? {file.closed}')

# Example 30: Using seek() and tell() after truncation
file = open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\test.txt', 'r')
file.seek(5)
print(f'Current file position: {file.tell()}')
content = file.read()
print(content)
file.close()
