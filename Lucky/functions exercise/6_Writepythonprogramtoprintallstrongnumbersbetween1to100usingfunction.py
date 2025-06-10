def strong_number(n):
    """Check if a number is a strong number."""
    sum_factorial = 0
    original_number = n
    
    while n > 0:
        digit = n % 10
        factorial = 1
        for i in range(1, digit + 1):
            factorial *= i
        sum_factorial += factorial
        n //= 10
    
    return sum_factorial == original_number
def print_strong_numbers(start, end):
    """Print all strong numbers in a given range."""
    strong_numbers = []
    for num in range(start, end + 1):
        if strong_number(num):
            strong_numbers.append(num)
    
    return strong_numbers
start = 1
end = 100   
strong_numbers = print_strong_numbers(start, end)
print(f"Strong numbers between {start} and {end}: {strong_numbers}")
