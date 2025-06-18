# ---------------------------------------

# Example 1: Checking File Permissions
import os

file_path = 'myfolder/test.txt'

# Check if the file is readable
print(f"Is '{file_path}' readable? ", os.access(file_path, os.R_OK))

# Check if the file is writable
print(f"Is '{file_path}' writable? ", os.access(file_path, os.W_OK))

# Check if the file is executable
print(f"Is '{file_path}' executable? ", os.access(file_path, os.X_OK))

# ---------------------------------------

# Example 2: Changing File Permissions to Read-Only
import os

file_path = 'myfolder/test.txt'

# Change the file permission to read-only
os.chmod(file_path, 0o444)

# Verify the change
print(f"Permissions for '{file_path}' changed to read-only.")

# ---------------------------------------

# Example 3: Changing File Permissions to Read and Write
import os

file_path = 'myfolder/test.txt'

# Change the file permission to read and write
os.chmod(file_path, 0o644)

# Verify the change
print(f"Permissions for '{file_path}' changed to read and write.")

# ---------------------------------------

# Example 4: Changing File Permissions to Executable
import os

file_path = 'myfolder/test.txt'

# Change the file permission to executable
os.chmod(file_path, 0o744)

# Verify the change
print(f"Permissions for '{file_path}' changed to executable.")

# ---------------------------------------

# Example 5: Setting Directory Permissions to Read, Write, and Execute
import os

dir_path = 'myfolder'

# Change the directory permissions to read, write, and execute
os.chmod(dir_path, 0o755)

# Verify the change
print(f"Permissions for directory '{dir_path}' changed to read, write, and execute.")

# ---------------------------------------

# Example 6: Checking Directory Permissions
import os

dir_path = 'myfolder'

# Check if the directory is readable
print(f"Is directory '{dir_path}' readable? ", os.access(dir_path, os.R_OK))

# Check if the directory is writable
print(f"Is directory '{dir_path}' writable? ", os.access(dir_path, os.W_OK))

# Check if the directory is executable
print(f"Is directory '{dir_path}' executable? ", os.access(dir_path, os.X_OK))

# ---------------------------------------

# Example 7: Changing File Owner (Unix-based systems only)
import os

file_path = 'myfolder/test.txt'

# Assuming you want to change the owner to user ID 1000 and group ID 1000
os.chown(file_path, 1000, 1000)

# Verify the change
print(f"Owner for '{file_path}' changed to user ID 1000 and group ID 1000.")

# ---------------------------------------

# Example 8: Setting umask for New Files and Directories
import os

# Set the umask to allow read and write permissions for new files
os.umask(0o022)

# Verify the change by creating a new file
with open('myfolder/new_test.txt', 'w') as f:
    f.write("This is a test file with new umask settings.")

print("New file 'myfolder/new_test.txt' created with umask 022.")

# ---------------------------------------

# Example 9: Checking File Existence and Permissions
import os

file_path = 'myfolder/test.txt'

# Check if the file exists
if os.path.exists(file_path):
    print(f"'{file_path}' exists.")
    # Check if the file is readable
    if os.access(file_path, os.R_OK):
        print(f"'{file_path}' is readable.")
    # Check if the file is writable
    if os.access(file_path, os.W_OK):
        print(f"'{file_path}' is writable.")
    # Check if the file is executable
    if os.access(file_path, os.X_OK):
        print(f"'{file_path}' is executable.")
else:
    print(f"'{file_path}' does not exist.")

# ---------------------------------------

# Example 10: Setting File Permissions Using stat Module
import os
import stat

file_path = 'myfolder/test.txt'

# Set the file to be readable and writable by the owner, readable by group and others
os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)

# Verify the change
print(f"Permissions for '{file_path}' set using stat module.")
