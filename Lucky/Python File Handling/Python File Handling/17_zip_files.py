
# --------------------------------------

# Example 1: Creating a ZIP File
import zipfile

def create_zip():
    with zipfile.ZipFile('myfolder/example1.zip', 'w') as zipf:
        zipf.writestr('file1.txt', 'This is the content of file1.txt')
        zipf.writestr('file2.txt', 'This is the content of file2.txt')
        

create_zip()

# --------------------------------------

# Example 2: Adding Files to an Existing ZIP File
import zipfile

def add_to_zip():
    with zipfile.ZipFile('myfolder/example2.zip', 'w') as zipf:
        zipf.write(__file__, 'example_script.py')


add_to_zip()

# --------------------------------------

# Example 3: Extracting a ZIP File
import zipfile

def extract_zip():
    with zipfile.ZipFile('myfolder/example1.zip', 'r') as zipf:
        zipf.extractall('extracted_files_example3')


extract_zip()

# --------------------------------------

# Example 4: Listing Contents of a ZIP File
import zipfile

def list_zip_contents():
    with zipfile.ZipFile('myfolder/example1.zip', 'r') as zipf:
        print(zipf.namelist())


list_zip_contents()

# --------------------------------------

# Example 5: Reading a File from a ZIP Archive
import zipfile

def read_file_in_zip():
    with zipfile.ZipFile('myfolder/example1.zip', 'r') as zipf:
        with zipf.open('file1.txt') as file:
            content = file.read()
            print(content.decode())


read_file_in_zip()

# --------------------------------------

# Example 6: Checking if a File Exists in a ZIP Archive
import zipfile

def check_file_in_zip():
    with zipfile.ZipFile('myfolder/example1.zip', 'r') as zipf:
        if 'file1.txt' in zipf.namelist():
            print('file1.txt exists in the ZIP archive')
        else:
            print('file1.txt does not exist in the ZIP archive')


check_file_in_zip()

# --------------------------------------

# Example 7: Getting Information about a File in a ZIP Archive
import zipfile

def get_file_info():
    with zipfile.ZipFile('myfolder/example1.zip', 'r') as zipf:
        info = zipf.getinfo('file1.txt')
        print(f"Filename: {info.filename}")
        print(f"File size: {info.file_size}")
        print(f"Compressed size: {info.compress_size}")


get_file_info()

# --------------------------------------

# Example 8: Deleting a File from a ZIP Archive (Create new ZIP without the file)
import zipfile

def delete_file_from_zip():
    with zipfile.ZipFile('myfolder/example1.zip', 'r') as zipf:
        files = zipf.namelist()
        files.remove('file1.txt')

    with zipfile.ZipFile('example8.zip', 'w') as zipf_new:
        for file in files:
            zipf_new.writestr(file, zipf.read(file))


delete_file_from_zip()

# --------------------------------------

# Example 9: Creating a ZIP File from Multiple Files
import zipfile

def create_zip_multiple_files():
    with zipfile.ZipFile('example9.zip', 'w') as zipf:
        zipf.write('file1.txt')
        zipf.write('file2.txt')
       
with open('file1.txt', 'w') as f:
    f.write('Content for file1.txt')
with open('file2.txt', 'w') as f:
    f.write('Content for file2.txt')
create_zip_multiple_files()

# --------------------------------------

# Example 10: Adding a Directory to a ZIP File
import zipfile
import os

def add_directory_to_zip(zipf, directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            zipf.write(os.path.join(root, file))

def create_zip_with_directory():
    with zipfile.ZipFile('example10.zip', 'w') as zipf:
        add_directory_to_zip(zipf, 'example_dir')


os.makedirs('example_dir', exist_ok=True)
with open('example_dir/file1.txt', 'w') as f:
    f.write('Content for file1.txt in example_dir')

create_zip_with_directory()

# --------------------------------------

# Example 11: Extracting Specific File from ZIP Archive
import zipfile

def extract_specific_file():
    with zipfile.ZipFile('example9.zip', 'r') as zipf:
        zipf.extract('file1.txt', 'extracted_files_example11')

extract_specific_file()

# --------------------------------------

# Example 12: Compressing Files with Compression Options
import zipfile

def compress_files_with_options():
    with zipfile.ZipFile('example12.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write('file1.txt')
        zipf.write('file2.txt')

compress_files_with_options()

# --------------------------------------

# Example 13: Password Protecting a ZIP File
import zipfile

def password_protect_zip():
    with zipfile.ZipFile('example13.zip', 'w') as zipf:
        zipf.write('file1.txt')
        zipf.setpassword(b'secret')

password_protect_zip()

# --------------------------------------

# Example 14: Extracting a Password Protected ZIP File
import zipfile

def extract_password_protected_zip():
    with zipfile.ZipFile('example13.zip', 'r') as zipf:
        zipf.setpassword(b'secret')
        zipf.extractall('extracted_files_example14')

extract_password_protected_zip()

# --------------------------------------

# Example 15: Creating ZIP File with Comment
import zipfile

def create_zip_with_comment():
    with zipfile.ZipFile('example15.zip', 'w') as zipf:
        zipf.write('file1.txt')
        zipf.comment = b'This is a comment for the ZIP file'

create_zip_with_comment()

# --------------------------------------

# Example 16: Reading ZIP File Comment
import zipfile

def read_zip_comment():
    with zipfile.ZipFile('example15.zip', 'r') as zipf:
        print(zipf.comment.decode())

read_zip_comment()
