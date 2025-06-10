def highest_common_factor(a, b):
    """
    Function to calculate the highest common factor (HCF) of two numbers using the Euclidean algorithm.
    
    Parameters:
    a (int): First number
    b (int): Second number
    
    Returns:
    int: The highest common factor of a and b
    """
    while b:
        a, b = b, a % b
    return a
def main():
    try:
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        if a <= 0 or b <= 0:
            print("Both numbers must be positive integers.")
            return
        hcf = highest_common_factor(a, b)
        print(f"The highest common factor of {a} and {b} is: {hcf}")
    except ValueError:
        print("Invalid input. Please enter valid integers.")
if __name__ == "__main__":
    main()
    