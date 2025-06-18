
# Example 1: Copying a File
import shutil

shutil.copy('myfolder/test.txt', 'myfolder/test_copy.txt')

# Example 2: Copying a File with Metadata
import shutil

shutil.copy2('myfolder/test.txt', 'myfolder/test_copy2.txt')

# Example 3: Copying a Directory
import shutil

shutil.copytree('myfolder', 'myfolder_copy')

# Example 4: Removing a Directory
import shutil

shutil.rmtree('myfolder_copy')

# Example 5: Moving a File
import shutil

shutil.move('myfolder/test.txt', 'myfolder/test_moved.txt')

# Example 6: Moving a Directory
import shutil

shutil.move('myfolder', 'myfolder_moved')

# Example 7: Renaming a File
import shutil
import os

os.rename('myfolder_moved/test_moved.txt', 'myfolder_moved/test_renamed.txt')

# Example 8: Renaming a Directory
import shutil
import os

os.rename('myfolder_moved', 'myfolder_renamed')

# Example 9: Archiving a Directory (ZIP)
import shutil

shutil.make_archive('myfolder_archive', 'zip', 'myfolder_renamed')

# Example 10: Extracting a ZIP Archive
import shutil
import zipfile

with zipfile.ZipFile('myfolder_archive.zip', 'r') as zip_ref:
    zip_ref.extractall('extracted_folder')

# Example 11: Archiving a Directory (TAR)
import shutil

shutil.make_archive('myfolder_archive_tar', 'gztar', 'myfolder_renamed')

# Example 12: Extracting a TAR Archive
import shutil
import tarfile

with tarfile.open('myfolder_archive_tar.tar.gz', 'r:gz') as tar_ref:
    tar_ref.extractall('extracted_tar_folder')

# Example 13: Copying File with Buffer Size
import shutil

shutil.copyfileobj(open('myfolder_renamed/test_renamed.txt', 'rb'), open('myfolder_renamed/test_buffered.txt', 'wb'), length=16*1024)

# Example 14: Creating a Disk Usage Report
import shutil

total, used, free = shutil.disk_usage('/')
print("Total: %d GiB" % (total // (2**30)))
print("Used: %d GiB" % (used // (2**30)))
print("Free: %d GiB" % (free // (2**30)))

# Example 15: Finding Available Disk Space
import shutil

total, used, free = shutil.disk_usage('myfolder_renamed')
print("Total: %d GiB" % (total // (2**30)))
print("Used: %d GiB" % (used // (2**30)))
print("Free: %d GiB" % (free // (2**30)))

# Example 16: Chown a File (Unix Only)
import shutil
import os

shutil.chown('myfolder_renamed/test_renamed.txt', user='username', group='groupname')

# Example 17: Comparing Files
import shutil

result = shutil.compare_files('myfolder_renamed/test_renamed.txt', 'myfolder_renamed/test_buffered.txt')
print(result)

# Example 18: Comparing Directories
import shutil

result = shutil.compare_dirs('myfolder_renamed', 'extracted_tar_folder')
print(result)

# Example 19: Getting File Metadata
import os

metadata = os.stat('myfolder_renamed/test_renamed.txt')
print(metadata)

# Example 20: Setting File Permissions
import os

os.chmod('myfolder_renamed/test_renamed.txt', 0o644)
