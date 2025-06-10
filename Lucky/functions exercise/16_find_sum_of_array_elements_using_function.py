def array_elements(arr):
    return arr
def sum_of_array(arr):
    """    This function takes an array as input and returns the sum of its elements.
    :param arr: List of elements
    :return: Sum of elements in the array
    """
    return sum(arr)
def main():
    try:
        n = int(input("Enter the number of elements in the array: "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        arr = []
        for i in range(n):
            element = int(input(f"Enter element {i + 1}: "))
            arr.append(element)
        elements = array_elements(arr)
        total_sum = sum_of_array(elements)
        print("The elements of the array are:", elements)
        print("The sum of the array elements is:", total_sum)
    except ValueError:
        print("Invalid input. Please enter valid integers.")
if __name__ == "__main__":
    main()