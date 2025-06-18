# File modes in Python define how a file should be opened for reading, writing, or appending. Here are the most commonly used file modes:

# r (Read)
    # Opens a file for reading only.
    # The file pointer is placed at the beginning of the file.
    # This is the default mode.
    # If the file does not exist, it raises a FileNotFoundError.

# w (Write)
    # Opens a file for writing.
    # If the file exists, its content is truncated (deleted).
    # If the file does not exist, a new file is created.
    # The file pointer is placed at the beginning of the file.

# a (Append)
    # Opens a file for appending.
    # If the file exists, the file pointer is at the end of the file.
    # If the file does not exist, a new file is created.
    # The file pointer is placed at the end of the file.

# r+ (Read and Write)
    # Opens a file for both reading and writing.
    # The file pointer is placed at the beginning of the file.
    # If the file does not exist, it raises a FileNotFoundError.

# w+ (Write and Read)
    # Opens a file for both writing and reading.
    # If the file exists, its content is truncated.
    # If the file does not exist, a new file is created.
    # The file pointer is placed at the beginning of the file.

# a+ (Append and Read)
    # Opens a file for both appending and reading.
    # If the file exists, the file pointer is at the end of the file.
    # If the file does not exist, a new file is created.
    # The file pointer is placed at the end of the file.



# Example 1: Read the entire file
with open('myfolder/test.txt', 'r') as file:
    content = file.read()
    print(content)

# Example 2: Read file line by line using readlines()
with open('myfolder/test.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

# Example 3: Write to a file (overwrite)
with open('myfolder/test.txt', 'w') as file:
    file.write("This is a new line.")

# Example 4: Append to a file
with open('myfolder/test.txt', 'a') as file:
    file.write("This is an appended line.")

# Example 5: Read the first line of the file
with open('myfolder/test.txt', 'r') as file:
    first_line = file.readline()
    print(first_line.strip())

# Example 6: Read file using a loop
with open('myfolder/test.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Example 7: Read and write (r+)
with open('myfolder/test.txt', 'r+') as file:
    content = file.read()
    file.write("Adding a new line with r+ mode.")
    print(content)

# Example 8: Write and read (w+)
with open('myfolder/test.txt', 'w+') as file:
    file.write("This is written with w+ mode.")
    file.seek(0)
    content = file.read()
    print(content)

# Example 9: Append and read (a+)
with open('myfolder/test.txt', 'a+') as file:
    file.write("This is written with a+ mode.")
    file.seek(0)
    content = file.read()
    print(content)

# Example 10: Write multiple lines to a file
lines = ["Line 1", "Line 2", "Line 3"]
with open('myfolder/test.txt', 'w') as file:
    file.writelines(lines)

# Example 11: Check if file is closed
with open('myfolder/test.txt', 'r') as file:
    print("Is file closed?", file.closed)
print("Is file closed?", file.closed)

# Example 12: Get file name and mode
with open('myfolder/test.txt', 'r') as file:
    print("File name:", file.name)
    print("File mode:", file.mode)

# Example 13: Read file with specific encoding
with open('myfolder/test.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

# Example 14: Write file with specific encoding
with open('myfolder/test.txt', 'w', encoding='utf-8') as file:
    file.write("This is a line with UTF-8 encoding.")

# Example 15: Using try-except for file operations
try:
    with open('myfolder/test.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found.")

# Example 16: Using 'with' statement for file operations
with open('myfolder/test.txt', 'r') as file:
    content = file.read()
    print(content)

# Example 17: Write if file exists, else create it
with open('myfolder/test.txt', 'w') as file:
    file.write("This is a new line.")

# Example 18: Write binary data to a file
with open('myfolder/test.txt', 'wb') as file:
    file.write(b"This is binary data.")

# Example 19: Read binary data from a file
with open('myfolder/test.txt', 'rb') as file:
    binary_content = file.read()
    print(binary_content)

# Example 20: Get file size
import os
file_size = os.path.getsize('myfolder/test.txt')
print("File size:", file_size, "bytes")

# Example 21: Check if file exists
import os
if os.path.exists('myfolder/test.txt'):
    print("File exists.")
else:
    print("File does not exist.")

# Example 22: Rename a file
import os
os.rename('myfolder/test.txt', 'renamed_test.txt')

# Example 23: Delete a file
import os
if os.path.exists('renamed_test.txt'):
    os.remove('renamed_test.txt')
    print("File deleted.")
else:
    print("File does not exist.")

# Example 24: Get file modification time
import os
import time
mod_time = os.path.getmtime('myfolder/test.txt')
print("Last modification time:", time.ctime(mod_time))

# Example 25: Create and write to a new file
with open('newfile.txt', 'w') as file:
    file.write("This is a new file.")