

# Example 7: Writing lines from a list with a loop using write()
lines_to_write = ["Loop line 1\n", "Loop line 2\n", "Loop line 3\n"]
with open("myfolder/test.txt", "w") as file:
    for line in lines_to_write:
        file.write(line)