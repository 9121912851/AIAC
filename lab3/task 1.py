import math

def math_factorial():
    """
    Calculates the factorial of a user-provided integer using the math module.
    """
    while True:
        try:
            n = int(input("Enter a non-negative integer to use the math module: "))
            if n < 0:
                print("Factorial is not defined for negative numbers. Please try again.")
            else:
                print(f"The factorial of {n} is {math.factorial(n)}")
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

math_factorial()
def recursive_factorial(n):
    """
    Calculates the factorial of a non-negative integer n using recursion.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)

# Example usage:
try:
    num = int(input("Enter a non-negative integer to use the recursive function: "))
    print(f"The factorial of {num} is {recursive_factorial(num)}")
except ValueError as e:
    print(e)
def user_input_factorial():
    """
    Prompts the user for a non-negative integer and prints its factorial.
    """
    while True:
        try:
            n = int(input("Enter a non-negative integer to calculate its factorial: "))
            if n < 0:
                print("Factorial is not defined for negative numbers. Please try again.")
            else:
                result = 1
                for i in range(2, n + 1):
                    result *= i
                print(f"The factorial of {n} is {result}")
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

user_input_factorial()
