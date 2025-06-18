
# Example 1: Writing Binary Data to a File
with open('myfolder/example1.bin', 'wb') as file:
    file.write(b'Hello, World!')

# Example 2: Reading Binary Data from a File
with open('myfolder/example1.bin', 'rb') as file:
    data = file.read()
    print(data)

# Example 3: Writing an Integer to a Binary File
number = 12345
with open('myfolder/example3.bin', 'wb') as file:
    file.write(number.to_bytes(4, byteorder='big'))

# Example 4: Reading an Integer from a Binary File
with open('myfolder/example3.bin', 'rb') as file:
    data = file.read()
    number = int.from_bytes(data, byteorder='big')
    print(number)

# Example 5: Writing a Float to a Binary File
import struct
float_number = 3.14
with open('myfolder/example5.bin', 'wb') as file:
    file.write(struct.pack('f', float_number))

# Example 6: Reading a Float from a Binary File
with open('myfolder/example5.bin', 'rb') as file:
    data = file.read()
    float_number = struct.unpack('f', data)[0]
    print(float_number)

# Example 7: Writing Multiple Integers to a Binary File
numbers = [10, 20, 30, 40]
with open('myfolder/example7.bin', 'wb') as file:
    for number in numbers:
        file.write(number.to_bytes(4, byteorder='big'))

# Example 8: Reading Multiple Integers from a Binary File
numbers = []
with open('myfolder/example7.bin', 'rb') as file:
    while chunk := file.read(4):
        numbers.append(int.from_bytes(chunk, byteorder='big'))
    print(numbers)

# Example 9: Writing a String as Binary Data
text = "Binary data"
with open('myfolder/example9.bin', 'wb') as file:
    file.write(text.encode())

# Example 10: Reading a String from Binary Data
with open('myfolder/example9.bin', 'rb') as file:
    data = file.read()
    text = data.decode()
    print(text)

# Example 11: Using struct to Pack and Write a Tuple
data = (1, b'A', 2.34)
with open('myfolder/example11.bin', 'wb') as file:
    file.write(struct.pack('i c f', *data))

# Example 12: Using struct to Unpack and Read a Tuple
with open('myfolder/example11.bin', 'rb') as file:
    data = file.read()
    unpacked_data = struct.unpack('i c f', data)
    print(unpacked_data)

# Example 13: Writing a List of Floats to a Binary File
floats = [1.1, 2.2, 3.3]
with open('myfolder/example13.bin', 'wb') as file:
    for number in floats:
        file.write(struct.pack('f', number))

# Example 14: Reading a List of Floats from a Binary File
floats = []
with open('myfolder/example13.bin', 'rb') as file:
    while chunk := file.read(4):
        floats.append(struct.unpack('f', chunk)[0])
    print(floats)

# Example 15: Writing a Dictionary to a Binary File
import pickle
data = {'name': 'Alice', 'age': 30, 'score': 95.5}
with open('myfolder/example15.bin', 'wb') as file:
    pickle.dump(data, file)

# Example 16: Reading a Dictionary from a Binary File
with open('myfolder/example15.bin', 'rb') as file:
    data = pickle.load(file)
    print(data)

# Example 17: Appending Binary Data to a File
with open('myfolder/example17.bin', 'wb') as file:
    file.write(b'Hello')

with open('myfolder/example17.bin', 'ab') as file:
    file.write(b' World')

with open('myfolder/example17.bin', 'rb') as file:
    data = file.read()
    print(data)

# Example 18: Writing and Reading a Complex Data Structure
data = (123, b'B', 4.56, "Python")
with open('myfolder/example18.bin', 'wb') as file:
    packed_data = struct.pack('i c f 6s', data[0], data[1], data[2], data[3].encode())
    file.write(packed_data)

with open('myfolder/example18.bin', 'rb') as file:
    data = file.read()
    unpacked_data = struct.unpack('i c f 6s', data)
    print(unpacked_data)

# Example 19: Handling Endianness in Binary Data
number = 12345
with open('myfolder/example19_big.bin', 'wb') as file:
    file.write(number.to_bytes(4, byteorder='big'))

with open('myfolder/example19_little.bin', 'wb') as file:
    file.write(number.to_bytes(4, byteorder='little'))

with open('myfolder/example19_big.bin', 'rb') as file:
    data = file.read()
    print(int.from_bytes(data, byteorder='big'))

with open('myfolder/example19_little.bin', 'rb') as file:
    data = file.read()
    print(int.from_bytes(data, byteorder='little'))

# Example 20: Writing and Reading Fixed-Size Records
record_size = 20
records = [b'First record', b'Second record', b'Third record']
with open('myfolder/example20.bin', 'wb') as file:
    for record in records:
        file.write(record.ljust(record_size))

with open('myfolder/example20.bin', 'rb') as file:
    while chunk := file.read(record_size):
        print(chunk.strip())
