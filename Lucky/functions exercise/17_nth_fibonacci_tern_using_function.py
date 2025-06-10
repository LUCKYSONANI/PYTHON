def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
def nth_fibonacci(n):
    """Return the nth Fibonacci number."""
    if n < 0:
        raise ValueError("Input should be a non-negative integer.")
    return fibonacci(n)
def main():
    try:
        n = int(input("Enter the position of the Fibonacci number to find (non-negative integer): "))
        if n < 0:
            print("Please enter a non-negative integer.")
            return
        result = nth_fibonacci(n)
        print(f"The {n}th Fibonacci number is: {result}")
    except ValueError as e:
        print(f"Invalid input: {e}")
if __name__ == "__main__":
    main()
    