def reverse_number(n: int) -> int:
    """
    Reverse the digits of a given integer.

    :param n: The integer to reverse.
    :return: The reversed integer.
    """
    reversed_num = 0
    is_negative = n < 0
    n = abs(n)

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10

    return -reversed_num if is_negative else reversed_num
def main():
    try:
        n = int(input("Enter an integer to reverse: "))
        reversed_num = reverse_number(n)
        print(f"The reversed number is: {reversed_num}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
if __name__ == "__main__":
    main()
    