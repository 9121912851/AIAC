def sum_even_odd(numbers):
    """
    Calculates the sum of even and odd numbers in a given iterable.

    Args:
        numbers (iterable of int): A sequence of integers to be processed.

    Returns:
        tuple: A tuple containing two integers:
            - The sum of even numbers.
            - The sum of odd numbers.

    Example:
        >>> sum_even_odd([1, 2, 3, 4, 5])
        (6, 9)
    """
    # Calculate the sum of even numbers using a generator expression.
    # n % 2 == 0 checks if n is even.
    even_sum = sum(n for n in numbers if n % 2 == 0)
    
    # Calculate the sum of odd numbers using a generator expression.
    # n % 2 != 0 checks if n is odd.
    odd_sum = sum(n for n in numbers if n % 2 != 0)
    return even_sum, odd_sum

numbers = [1, 2, 3, 4, 5, 6]
even_sum, odd_sum = sum_even_odd(numbers)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
