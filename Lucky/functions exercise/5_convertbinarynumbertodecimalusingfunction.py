# 5. Write C Program to convert binary number to decimal using function.
def binary_to_decimal(binary_str):
    decimal_value = 0
    power = 0
    
    # Reverse the binary string to process from least significant bit
    for digit in reversed(binary_str):
        if digit == '1':
            decimal_value += 2 ** power
        power += 1
    
    return decimal_value
binary_input = input("Enter a binary number to convert to decimal: ")
try:
    # Validate input to ensure it only contains '0' and '1'
    if not all(digit in '01' for digit in binary_input):
        raise ValueError("Input must be a valid binary number (only 0s and 1s).")
    
    decimal_output = binary_to_decimal(binary_input)
    print(f"The decimal representation of binary {binary_input} is {decimal_output}.")
except ValueError as e:
    print(e)
