def lowest_common_multiple(x, y):
    """Calculate the lowest common multiple (LCM) of two numbers."""
    def gcd(a, b):
        """Calculate the greatest common divisor (GCD) using Euclid's algorithm."""
        while b:
            a, b = b, a % b
        return a

    return abs(x * y) // gcd(x, y)
def main():
    try:
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        if x <= 0 or y <= 0:
            print("Both numbers must be positive integers.")
            return
        lcm = lowest_common_multiple(x, y)
        print(f"The lowest common multiple of {x} and {y} is: {lcm}")
    except ValueError:
        print("Invalid input. Please enter valid integers.")
if __name__ == "__main__":
    main()