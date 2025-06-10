def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_numbers_between_1_and_100():
    """Print all prime numbers between 1 and 100."""
    prime_numbers = []
    for num in range(1, 101):
        if isprime(num):
            prime_numbers.append(num)
    
    return prime_numbers
start = 1
end = 100
prime_numbers = prime_numbers_between_1_and_100()
print(f"Prime numbers between {start} and {end}: {prime_numbers}")
