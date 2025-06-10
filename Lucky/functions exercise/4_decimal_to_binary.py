def dec(a):
    if a < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    if a == 0:
        return "0"
    
    binary = ""
    while a > 0:
        binary = str(a % 2) + binary
        a //= 2
    
    return binary
a=int(input("Enter a non-negative integer to convert to binary: "))
try:
    result = dec(a)
    print(f"The binary representation of {a} is {result}.")     
except ValueError as e:
    print(e)
    

