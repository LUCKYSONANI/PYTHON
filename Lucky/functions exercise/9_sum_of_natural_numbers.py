def natural_numbers_sum(n):
    """
    Calculate the sum of the first n natural numbers.
    
    :param n: The number of natural numbers to sum.
    :return: The sum of the first n natural numbers.
    """
    if n < 1:
        return 0
    return n * (n + 1) // 2
def main():
    try:
        n = int(input("Enter the number of natural numbers to sum: "))
        if n < 1:
            print("Please enter a positive integer.")
            return
        result = natural_numbers_sum(n)
        print(f"The sum of the first {n} natural numbers is: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
if __name__ == "__main__":
    main()
# This code calculates the sum of the first n natural numbers.
# It uses the formula n * (n + 1) // 2 for efficiency.