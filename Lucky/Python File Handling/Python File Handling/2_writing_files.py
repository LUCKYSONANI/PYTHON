
# 'w' is a file mode, used to write into file

# Example 1: Writing a single line using write()
with open("myfolder/test.txt", "w") as file:
    file.write("This is a new first line.\n")

# Example 2: Writing multiple lines using write() method
with open("myfolder/test.txt", "w") as file:
    file.write("Line 1\n")
    file.write("Line 2\n")
    file.write("Line 3\n")

# Example 3: Writing a list of lines using writelines() method
lines = ["Line A\n", "Line B\n", "Line C\n"]
with open("myfolder/test.txt", "w") as file:
    file.writelines(lines)

# Example 4: Appending a single line using write()
with open("myfolder/test.txt", "a") as file:
    file.write("Appending a new line.\n")

# Example 5: Appending multiple lines using write()
with open("myfolder/test.txt", "a") as file:
    file.write("Appending line 1\n")
    file.write("Appending line 2\n")

# Example 6: Appending a list of lines using writelines()
more_lines = ["Append A\n", "Append B\n", "Append C\n"]
with open("myfolder/test.txt", "a") as file:
    file.writelines(more_lines)

# Example 7: Writing lines from a list with a loop using write()
lines_to_write = ["Loop line 1\n", "Loop line 2\n", "Loop line 3\n"]
with open("myfolder/test.txt", "w") as file:
    for line in lines_to_write:
        file.write(line)

# Example 8: Writing a string with special characters using write()
special_chars = "Special characters: !@#$%^&*()\n"
with open("myfolder/test.txt", "w") as file:
    file.write(special_chars)

# Example 9: Writing a string with numbers using write()
numbers = "1234567890\n"
with open("myfolder/test.txt", "w") as file:
    file.write(numbers)

# Example 10: Writing a string with mixed content using write()
mixed_content = "Mix: ABC 123 !@#\n"
with open("myfolder/test.txt", "w") as file:
    file.write(mixed_content)

# Example 11: Writing lines from a dictionary using writelines()
dictionary = {1: "Dict line 1\n", 2: "Dict line 2\n", 3: "Dict line 3\n"}
with open("myfolder/test.txt", "w") as file:
    file.writelines(dictionary.values())

# Example 12: Writing lines from a tuple using writelines()
tuple_lines = ("Tuple line 1\n", "Tuple line 2\n", "Tuple line 3\n")
with open("myfolder/test.txt", "w") as file:
    file.writelines(tuple_lines)

# Example 13: Writing lines with varying lengths using write()
with open("myfolder/test.txt", "w") as file:
    file.write("Short\n")
    file.write("A bit longer line\n")
    file.write("This is the longest line in this example.\n")

# Example 14: Writing lines with newline characters using writelines()
newlines = ["Line with\nnewline\ncharacter\n", "Another line\n"]
with open("myfolder/test.txt", "w") as file:
    file.writelines(newlines)

# Example 15: Writing lines from a generator using writelines()
def line_generator():
    for i in range(1, 4):
        yield f"Generated line {i}\n"

with open("myfolder/test.txt", "w") as file:
    file.writelines(line_generator())

# Example 16: Writing formatted strings using write()
name = "Alice"
age = 30
with open("myfolder/test.txt", "w") as file:
    file.write(f"Name: {name}, Age: {age}\n")

# Example 17: Writing lines with different encodings using write()
with open("myfolder/test.txt", "w", encoding="utf-8") as file:
    file.write("UTF-8 encoding line\n")

# Example 18: Writing a large amount of text using write()
large_text = "This is a large text. " * 100
with open("myfolder/test.txt", "w") as file:
    file.write(large_text + "\n")

# Example 19: Writing lines from a user input using write()
user_input = input("Enter a line to write to the file: ")
with open("myfolder/test.txt", "w") as file:
    file.write(user_input + "\n")

# Example 20: Writing lines from a file using writelines()
source_file = "source.txt"
with open(source_file, "w") as src:
    src.write("Source line 1\nSource line 2\nSource line 3\n")

with open(source_file, "r") as src:
    lines = src.readlines()

with open("myfolder/test.txt", "w") as dest:
    dest.writelines(lines)
