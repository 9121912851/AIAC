def sort_ascending(numbers):
    """
    Returns a new list containing the numbers from the input list sorted in ascending order.
    The original list is not modified.
    """
    return sorted(numbers)

if __name__ == "__main__":
    user_input = input("Enter numbers separated by spaces: ")
    try:
        num_list = [float(x) for x in user_input.strip().split()]
        sorted_list = sort_ascending(num_list)
        print("Sorted list in ascending order:", sorted_list)
    except ValueError:
        print("Invalid input. Please enter only numbers separated by spaces.")
