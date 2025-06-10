def array_elements(arr):
    """
    This function takes an array as input and returns its elements.
    
    :param arr: List of elements
    :return: List of elements in the array
    """
    return arr
def main():
    try:
        n = int(input("Enter the number of elements in the array: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        arr = []
        for i in range(n):
            element = input(f"Enter element {i + 1}: ")
            arr.append(element)
        elements = array_elements(arr)
        print("The elements of the array are:", elements)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
if __name__ == "__main__":
    main()