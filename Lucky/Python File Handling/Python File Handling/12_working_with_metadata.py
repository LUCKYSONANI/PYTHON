
# ----------------------------------------

# Example 1: Checking if a File Exists
import os

file_path = 'myfolder/test.txt'
if os.path.exists(file_path):
    print(f"File '{file_path}' exists.")
else:
    print(f"File '{file_path}' does not exist.")

# ----------------------------------------

# Example 2: Getting File Size
file_path = 'myfolder/test.txt'
file_size = os.path.getsize(file_path)
print(f"Size of '{file_path}': {file_size} bytes")

# ----------------------------------------

# Example 3: Getting File Creation Time
import os
import time

file_path = 'myfolder/test.txt'
creation_time = os.path.getctime(file_path)
print(f"Creation time of '{file_path}': {time.ctime(creation_time)}")

# ----------------------------------------

# Example 4: Getting File Modification Time
file_path = 'myfolder/test.txt'
modification_time = os.path.getmtime(file_path)
print(f"Modification time of '{file_path}': {time.ctime(modification_time)}")

# ----------------------------------------

# Example 5: Getting File Access Time
file_path = 'myfolder/test.txt'
access_time = os.path.getatime(file_path)
print(f"Access time of '{file_path}': {time.ctime(access_time)}")

# ----------------------------------------

# Example 6: Checking if Path is a File
file_path = 'myfolder/test.txt'
if os.path.isfile(file_path):
    print(f"'{file_path}' is a file.")
else:
    print(f"'{file_path}' is not a file.")

# ----------------------------------------

# Example 7: Checking if Path is a Directory
directory_path = 'myfolder'
if os.path.isdir(directory_path):
    print(f"'{directory_path}' is a directory.")
else:
    print(f"'{directory_path}' is not a directory.")

# ----------------------------------------

# Example 8: Getting File Permissions
file_path = 'myfolder/test.txt'
permissions = oct(os.stat(file_path).st_mode)[-3:]
print(f"Permissions of '{file_path}': {permissions}")

# ----------------------------------------

# Example 9: Changing File Permissions
import stat

file_path = 'myfolder/test.txt'
os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
print(f"Changed permissions of '{file_path}' to '644'.")

# ----------------------------------------

# Example 10: Getting File Owner
# ! Work only on linux / unix


import pwd

file_path = 'myfolder/test.txt'
file_stat = os.stat(file_path)
owner = pwd.getpwuid(file_stat.st_uid).pw_name
print(f"Owner of '{file_path}': {owner}")

# ----------------------------------------

# Example 11: Getting File Group
# ! Work only on linux / unix

import grp

file_path = 'myfolder/test.txt'
file_stat = os.stat(file_path)
group = grp.getgrgid(file_stat.st_gid).gr_name
print(f"Group of '{file_path}': {group}")

# ----------------------------------------

# Example 12: Checking if File is Readable
file_path = 'myfolder/test.txt'
if os.access(file_path, os.R_OK):
    print(f"'{file_path}' is readable.")
else:
    print(f"'{file_path}' is not readable.")

# ----------------------------------------

# Example 13: Checking if File is Writable
file_path = 'myfolder/test.txt'
if os.access(file_path, os.W_OK):
    print(f"'{file_path}' is writable.")
else:
    print(f"'{file_path}' is not writable.")

# ----------------------------------------

# Example 14: Checking if File is Executable
file_path = 'myfolder/test.txt'
if os.access(file_path, os.X_OK):
    print(f"'{file_path}' is executable.")
else:
    print(f"'{file_path}' is not executable.")

# ----------------------------------------

# Example 15: Getting Absolute File Path
file_path = 'myfolder/test.txt'
absolute_path = os.path.abspath(file_path)
print(f"Absolute path of '{file_path}': {absolute_path}")

# ----------------------------------------

# Example 16: Getting Directory Name of File
file_path = 'myfolder/test.txt'
directory_name = os.path.dirname(file_path)
print(f"Directory name of '{file_path}': {directory_name}")

# ----------------------------------------

# Example 17: Getting Base Name of File
file_path = 'myfolder/test.txt'
base_name = os.path.basename(file_path)
print(f"Base name of '{file_path}': {base_name}")

# ----------------------------------------

# Example 18: Splitting File Path into Directory and Base Name
file_path = 'myfolder/test.txt'
directory_name, base_name = os.path.split(file_path)
print(f"Directory name: {directory_name}, Base name: {base_name}")

# ----------------------------------------

# Example 19: Getting File Extension
file_path = 'myfolder/test.txt'
file_name, file_extension = os.path.splitext(file_path)
print(f"File extension of '{file_path}': {file_extension}")

# ----------------------------------------

# Example 20: Checking if File is a Symbolic Link
file_path = 'myfolder/test.txt'
if os.path.islink(file_path):
    print(f"'{file_path}' is a symbolic link.")
else:
    print(f"'{file_path}' is not a symbolic link.")
