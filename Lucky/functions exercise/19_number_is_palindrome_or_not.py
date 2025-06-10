def palindrome(n):
    # Convert the number to string
    s = str(n)
    # Check if the string is equal to its reverse
    return s == s[::-1]
def main():
    try:
        n = int(input("Enter a number to check if it is a palindrome: "))
        if palindrome(n):
            print(f"{n} is a palindrome.")
        else:
            print(f"{n} is not a palindrome.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
if __name__ == "__main__":
    main()