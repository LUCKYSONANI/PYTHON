
# Example 4: Reading an Integer from a Binary File
with open('C:\\Users\\r41\\Desktop\\lucky\\PYTHON\\Lucky\\Python File Handling\\myfolder\\example3.bin', 'rb') as file:
    data = file.read()
    number = int.from_bytes(data, byteorder='big')
    print(number)