
# -------------------------------------

# Example 1: Deleting a Single File
import os
if os.path.exists("myfolder/test.txt"):
    os.remove("myfolder/test.txt")
    print("File 'test.txt' deleted successfully.")
else:
    print("The file does not exist.")

# -------------------------------------

# Example 2: Deleting a Single File with Error Handling
import os
try:
    os.remove("myfolder/test.txt")
    print("File 'test.txt' deleted successfully.")
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"Error: {e}")

# -------------------------------------

# Example 3: Deleting a Directory
import os
try:
    os.rmdir("myfolder")
    print("Directory 'myfolder' deleted successfully.")
except FileNotFoundError:
    print("The directory does not exist.")
except OSError:
    print("Directory not empty or other error.")
except Exception as e:
    print(f"Error: {e}")

# -------------------------------------

# Example 4: Deleting a Directory and its Contents
import shutil
try:
    shutil.rmtree("myfolder")
    print("Directory 'myfolder' and its contents deleted successfully.")
except FileNotFoundError:
    print("The directory does not exist.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"Error: {e}")

# -------------------------------------

# Example 5: Deleting a File Using Pathlib
from pathlib import Path
file_path = Path("myfolder/test.txt")
try:
    file_path.unlink()
    print("File 'test.txt' deleted successfully.")
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print(f"Error: {e}")

# -------------------------------------

# Example 6: Deleting a Directory Using Pathlib
from pathlib import Path
dir_path = Path("myfolder")
try:
    dir_path.rmdir()
    print("Directory 'myfolder' deleted successfully.")
except FileNotFoundError:
    print("The directory does not exist.")
except OSError:
    print("Directory not empty or other error.")
except Exception as e:
    print(f"Error: {e}")

# -------------------------------------

# Example 7: Deleting Multiple Files in a Directory
import os
file_list = ["myfolder/test1.txt", "myfolder/test2.txt", "myfolder/test3.txt"]
for file_path in file_list:
    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
    except PermissionError:
        print(f"Permission denied for file '{file_path}'.")
    except Exception as e:
        print(f"Error deleting file '{file_path}': {e}")

# -------------------------------------

# Example 8: Deleting Files with Specific Extension
import os
import glob
files = glob.glob("myfolder/*.txt")
for file_path in files:
    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")

# -------------------------------------

# Example 9: Deleting Empty Directories Recursively
import os
for root, dirs, files in os.walk("myfolder", topdown=False):
    for name in dirs:
        dir_path = os.path.join(root, name)
        try:
            os.rmdir(dir_path)
            print(f"Directory '{dir_path}' deleted successfully.")
        except OSError:
            print(f"Error deleting directory '{dir_path}'.")

# -------------------------------------

# Example 10: Deleting All Files in a Directory
import os
import glob
files = glob.glob("myfolder/*")
for file_path in files:
    try:
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"File '{file_path}' deleted successfully.")
        elif os.path.isdir(file_path):
            os.rmdir(file_path)
            print(f"Directory '{file_path}' deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")

# -------------------------------------

# Example 11: Deleting All Files and Directories in a Directory
import shutil
import os
for root, dirs, files in os.walk("myfolder"):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        try:
            os.remove(file_path)
            print(f"File '{file_path}' deleted successfully.")
        except Exception as e:
            print(f"Error: {e}")
    for dir_name in dirs:
        dir_path = os.path.join(root, dir_name)
        try:
            shutil.rmtree(dir_path)
            print(f"Directory '{dir_path}' deleted successfully.")
        except Exception as e:
            print(f"Error: {e}")

# -------------------------------------

# Example 12: Deleting a File After Checking Size
import os
file_path = "myfolder/test.txt"
try:
    if os.path.getsize(file_path) > 0:
        os.remove(file_path)
        print("File 'test.txt' deleted successfully.")
    else:
        print("File is empty, not deleting.")
except FileNotFoundError:
    print("The file does not exist.")
except Exception as e:
    print(f"Error: {e}")

# -------------------------------------

# Example 13: Deleting Read-Only Files
import os
import stat
file_path = "myfolder/test.txt"
try:
    os.chmod(file_path, stat.S_IWRITE)
    os.remove(file_path)
    print("Read-only file 'test.txt' deleted successfully.")
except FileNotFoundError:
    print("The file does not exist.")
except Exception as e:
    print(f"Error: {e}")

# -------------------------------------

# Example 14: Deleting Files Created Before a Certain Date
import os
import time
import glob
cutoff = time.time() - (7 * 86400)  # 7 days ago
files = glob.glob("myfolder/*")
for file_path in files:
    if os.path.isfile(file_path):
        if os.path.getmtime(file_path) < cutoff:
            try:
                os.remove(file_path)
                print(f"Old file '{file_path}' deleted successfully.")
            except Exception as e:
                print(f"Error: {e}")

# -------------------------------------

# Example 15: Deleting Files with Specific Pattern
import os
import glob
files = glob.glob("myfolder/test*.txt")
for file_path in files:
    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")

# -------------------------------------

# Example 16: Using Tempfile for Deleting Temporary Files
import os
import tempfile
with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
    tmp_file.write(b'This is a temp file')
try:
    os.remove(tmp_file.name)
    print("Temporary file deleted successfully.")
except Exception as e:
    print(f"Error: {e}")

# -------------------------------------

# Example 17: Deleting a Directory Tree with Specific Depth
import os
import shutil
def delete_tree(path, depth):
    if depth < 0:
        return
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            delete_tree(item_path, depth - 1)
            shutil.rmtree(item_path)
            print(f"Directory '{item_path}' deleted successfully.")
        else:
            os.remove(item_path)
            print(f"File '{item_path}' deleted successfully.")
delete_tree("myfolder", 1)

# -------------------------------------

# Example 18: Using Pathlib for Deleting Files Recursively
from pathlib import Path
import shutil
dir_path = Path("myfolder")
for item in dir_path.rglob('*'):
    try:
        if item.is_file():
            item.unlink()
            print(f"File '{item}' deleted successfully.")
        elif item.is_dir():
            shutil.rmtree(item)
            print(f"Directory '{item}' deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")

# -------------------------------------

# Example 19: Deleting Files Larger Than a Specific Size
import os
import glob
files = glob.glob("myfolder/*")
for file_path in files:
    if os.path.isfile(file_path) and os.path.getsize(file_path) > 1024:  # 1 KB
        try:
            os.remove(file_path)
            print(f"Large file '{file_path}' deleted successfully.")
        except Exception as e:
            print(f"Error: {e}")

# -------------------------------------

# Example 20: Deleting Files with Specific Permissions
import os
import stat
file_path = "myfolder/test.txt"
try:
    if os.stat(file_path).st_mode & stat.S_IREAD:
        os.remove(file_path)
        print("Read-only file 'test.txt' deleted successfully.")
    else:
        print("File does not have the specified permissions.")
except FileNotFoundError:
    print("The file does not exist.")
except Exception as e:
    print(f"Error: {e}")
