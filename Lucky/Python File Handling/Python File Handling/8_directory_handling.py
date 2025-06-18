
# Example 1: Overview of Directory Handling
import os

print("Current Working Directory:", os.getcwd())

# Example 2: Creating a Directory
os.mkdir('example_dir')
print("Directory 'example_dir' created")

# Example 3: Removing a Directory
os.rmdir('example_dir')
print("Directory 'example_dir' removed")

# Example 4: Creating Nested Directories
os.makedirs('nested_dir/sub_dir')
print("Nested directories 'nested_dir/sub_dir' created")

# Example 5: Removing Nested Directories
os.removedirs('nested_dir/sub_dir')
print("Nested directories 'nested_dir/sub_dir' removed")

# Example 6: Listing Files and Directories in the Current Directory
print("List of files and directories:", os.listdir('.'))

# Example 7: Changing the Current Directory
os.mkdir('example_dir')
os.chdir('example_dir')
print("Changed current directory to 'example_dir'")
os.chdir('..')
os.rmdir('example_dir')
print("Changed back to the original directory")

# Example 8: Handling Directory Exceptions (Directory Exists)
try:
    os.mkdir('example_dir')
    os.mkdir('example_dir')  # This will cause an exception
except FileExistsError:
    print("Directory 'example_dir' already exists")
finally:
    os.rmdir('example_dir')

# Example 9: Handling Directory Exceptions (Directory Not Found)
try:
    os.rmdir('non_existent_dir')  # This will cause an exception
except FileNotFoundError:
    print("Directory 'non_existent_dir' not found")

# Example 10: Creating a Temporary Directory
import tempfile

with tempfile.TemporaryDirectory() as temp_dir:
    print("Temporary directory created:", temp_dir)

# Example 11: Checking if a Directory Exists
print("Does 'example_dir' exist?", os.path.exists('example_dir'))

# Example 12: Renaming a Directory
os.mkdir('old_dir')
os.rename('old_dir', 'new_dir')
print("Directory renamed from 'old_dir' to 'new_dir'")
os.rmdir('new_dir')

# Example 13: Getting the Absolute Path of a Directory
print("Absolute path of current directory:", os.path.abspath('.'))

# Example 14: Walking Through a Directory Tree
os.makedirs('example_dir/sub_dir')
for root, dirs, files in os.walk('example_dir'):
    print("Root:", root)
    print("Directories:", dirs)
    print("Files:", files)
os.removedirs('example_dir/sub_dir')

# Example 15: Getting the Size of a Directory
def get_dir_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

os.makedirs('example_dir/sub_dir')
print("Size of 'example_dir':", get_dir_size('example_dir'), "bytes")
os.removedirs('example_dir/sub_dir')

# Example 16: Listing Only Directories
print("List of directories:", [d for d in os.listdir('.') if os.path.isdir(d)])

# Example 17: Listing Only Files
print("List of files:", [f for f in os.listdir('.') if os.path.isfile(f)])

# Example 18: Creating a Directory with Permissions
os.mkdir('example_dir', mode=0o700)
print("Directory 'example_dir' created with permissions 700")
os.rmdir('example_dir')

# Example 19: Changing Directory Permissions
os.mkdir('example_dir')
os.chmod('example_dir', 0o755)
print("Permissions of 'example_dir' changed to 755")
os.rmdir('example_dir')

# Example 20: Copying a Directory
import shutil

os.makedirs('example_dir/sub_dir')
shutil.copytree('example_dir', 'copied_dir')
print("Directory 'example_dir' copied to 'copied_dir'")
shutil.rmtree('example_dir')
shutil.rmtree('copied_dir')

# Example 21: Moving a Directory
os.mkdir('example_dir')
shutil.move('example_dir', 'moved_dir')
print("Directory 'example_dir' moved to 'moved_dir'")
os.rmdir('moved_dir')

# Example 22: Creating Multiple Directories at Once
os.makedirs('parent_dir/child_dir')
print("Directories 'parent_dir/child_dir' created")
os.removedirs('parent_dir/child_dir')

# Example 23: Checking Directory Read/Write Permissions
os.mkdir('example_dir')
print("Can read 'example_dir'?", os.access('example_dir', os.R_OK))
print("Can write to 'example_dir'?", os.access('example_dir', os.W_OK))
os.rmdir('example_dir')

# Example 24: Using pathlib to Handle Directories
from pathlib import Path

path = Path('example_dir')
path.mkdir()
print("Directory 'example_dir' created using pathlib")
path.rmdir()
print("Directory 'example_dir' removed using pathlib")

# Example 25: Getting the Parent Directory
path = Path('example_dir/sub_dir')
print("Parent directory of 'example_dir/sub_dir':", path.parent)

# Example 26: Checking if a Path is a Directory
path = Path('example_dir')
path.mkdir()
print("Is 'example_dir' a directory?", path.is_dir())
path.rmdir()

# Example 27: Iterating Over Directory Contents
os.mkdir('example_dir')
Path('example_dir/file1.txt').touch()
Path('example_dir/file2.txt').touch()
for item in path.iterdir():
    print("Item in 'example_dir':", item)
shutil.rmtree('example_dir')

# Example 28: Creating Temporary Directories with pathlib
with tempfile.TemporaryDirectory() as temp_dir:
    path = Path(temp_dir)
    print("Temporary directory created with pathlib:", path)

# Example 29: Resolving the Absolute Path with pathlib
path = Path('example_dir')
path.mkdir()
print("Absolute path of 'example_dir':", path.resolve())
path.rmdir()

# Example 30: Checking if a Directory is Empty
path = Path('example_dir')
path.mkdir()
print("Is 'example_dir' empty?", not any(path.iterdir()))
path.rmdir()

# Example 31: Comparing Directory Contents
path1 = Path('dir1')
path2 = Path('dir2')
path1.mkdir()
path2.mkdir()
(Path('dir1/file1.txt')).touch()
(Path('dir2/file1.txt')).touch()
print("Contents of 'dir1' and 'dir2' are the same?", set(path1.iterdir()) == set(path2.iterdir()))
shutil.rmtree('dir1')
shutil.rmtree('dir2')

# Example 32: Finding Files by Extension
os.mkdir('example_dir')
(Path('example_dir/file1.txt')).touch()
(Path('example_dir/file2.py')).touch()
txt_files = list(Path('example_dir').glob('*.txt'))
print("Text files in 'example_dir':", txt_files)
shutil.rmtree('example_dir')

# Example 33: Reading the Contents of a Directory Recursively
path = Path('example_dir')
path.mkdir()
(Path('example_dir/file1.txt')).touch()
(Path('example_dir/sub_dir')).mkdir()
(Path('example_dir/sub_dir/file2.txt')).touch()
for p in path.rglob('*'):
    print("Item in 'example_dir' recursively:", p)
shutil.rmtree('example_dir')

# Example 34: Flattening a Directory Structure
os.makedirs('example_dir/sub_dir')
(Path('example_dir/sub_dir/file1.txt')).touch()
for file in Path('example_dir/sub_dir').iterdir():
    shutil.move(str(file), 'example_dir')
shutil.rmtree('example_dir/sub_dir')
print("Directory structure of 'example_dir' flattened")
shutil.rmtree('example_dir')

# Example 35: Checking Disk Usage
usage = shutil.disk_usage('/')
print("Total:", usage.total, "bytes")
print("Used:", usage.used, "bytes")
print("Free:", usage.free, "bytes")
