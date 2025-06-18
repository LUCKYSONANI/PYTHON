
# Example 1: Copying a File
import shutil
shutil.copy('myfolder/test.txt', 'myfolder/test_copy.txt')

# Example 2: Copying a File with Metadata
import shutil
shutil.copy2('myfolder/test.txt', 'myfolder/test_copy2.txt')

# Example 3: Copying a Directory
import shutil
shutil.copytree('myfolder', 'myfolder_copy')

# Example 4: Moving a File
import shutil
shutil.move('myfolder/test.txt', 'myfolder/test_moved.txt')

# Example 5: Moving a Directory
import shutil
shutil.move('myfolder', 'myfolder_moved')

# Example 6: Renaming a File
import os
os.rename('myfolder/test.txt', 'myfolder/test_renamed.txt')

# Example 7: Renaming a Directory
import os
os.rename('myfolder', 'myfolder_renamed')

# Example 8: Copying a File to Another Directory
import shutil
shutil.copy('myfolder/test.txt', 'myfolder/subfolder/test_copy.txt')

# Example 9: Moving a File to Another Directory
import shutil
shutil.move('myfolder/test.txt', 'myfolder/subfolder/test_moved.txt')

# Example 10: Copying a Directory to Another Directory
import shutil
shutil.copytree('myfolder', 'backup/myfolder_copy')

# Example 11: Moving a Directory to Another Directory
import shutil
shutil.move('myfolder', 'backup/myfolder_moved')

# Example 12: Copying Multiple Files
import shutil
shutil.copy('myfolder/test1.txt', 'myfolder/test1_copy.txt')
shutil.copy('myfolder/test2.txt', 'myfolder/test2_copy.txt')

# Example 13: Moving Multiple Files
import shutil
shutil.move('myfolder/test1.txt', 'myfolder/test1_moved.txt')
shutil.move('myfolder/test2.txt', 'myfolder/test2_moved.txt')

# Example 14: Renaming Multiple Files
import os
os.rename('myfolder/test1.txt', 'myfolder/test1_renamed.txt')
os.rename('myfolder/test2.txt', 'myfolder/test2_renamed.txt')

# Example 15: Copying a File with a New Name
import shutil
shutil.copy('myfolder/test.txt', 'myfolder/test_newname.txt')

# Example 16: Moving a File with a New Name
import shutil
shutil.move('myfolder/test.txt', 'myfolder/test_newname_moved.txt')

# Example 17: Copying a File and Changing Permissions
import shutil
import os
shutil.copy('myfolder/test.txt', 'myfolder/test_copy.txt')
os.chmod('myfolder/test_copy.txt', 0o644)

# Example 18: Moving a File and Changing Permissions
import shutil
import os
shutil.move('myfolder/test.txt', 'myfolder/test_moved.txt')
os.chmod('myfolder/test_moved.txt', 0o644)

# Example 19: Copying a Directory and Excluding Certain Files
import shutil
import os

def ignore_files(dir, files):
    return [f for f in files if f.endswith('.log')]

shutil.copytree('myfolder', 'myfolder_copy_exclude', ignore=ignore_files)

# Example 20: Moving a Directory and Excluding Certain Files
import shutil
import os

def ignore_files(dir, files):
    return [f for f in files if f.endswith('.log')]

shutil.copytree('myfolder', 'myfolder_temp', ignore=ignore_files)
shutil.move('myfolder_temp', 'myfolder_moved_exclude')
