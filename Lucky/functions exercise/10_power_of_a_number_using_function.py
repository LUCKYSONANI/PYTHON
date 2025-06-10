def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result
def main():
    try:
        base = float(input("Enter the base number: "))
        exponent = int(input("Enter the exponent (non-negative integer): "))
        if exponent < 0:
            print("Exponent must be a non-negative integer.")
            return
        result = power(base, exponent)
        print(f"{base} raised to the power of {exponent} is: {result}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
if __name__ == "__main__":
    main()