def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def main():
    try:
        n = int(input("Enter a non-negative integer to calculate its factorial: "))
        if n < 0:
            print("Please enter a non-negative integer.")
            return
        result = factorial(n)
        print(f"The factorial of {n} is: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer.")
if __name__ == "__main__":
    main()
    