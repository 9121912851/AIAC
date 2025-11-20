# Method 1: Using modulo operator
def is_even_mod(n):
    """Check even/odd using modulo operator"""
    # If remainder is 0, number is even
    return n % 2 == 0


# Method 2: Using bitwise operator
def is_even_bitwise(n):
    """Check even/odd using bitwise AND"""
    # Even numbers have last bit 0, odd numbers have last bit 1
    return (n & 1) == 0


# Method 3: Using repeated subtraction
def is_even_sub(n):
    """Check even/odd using repeated subtraction"""
    # Keep subtracting 2 until we reach 0 (even) or 1 (odd)
    while n > 1:
        n -= 2
    return n == 0


# ----------------------------
# Test Cases
# ----------------------------

nums = [4, 7, 10, 13]

print("Modulo Method:")
for x in nums:
    print(x, "Even?" , is_even_mod(x))

print("\nBitwise Method:")
for x in nums:
    print(x, "Even?" , is_even_bitwise(x))

print("\nRepeated Subtraction Method:")
for x in nums:
    print(x, "Even?" , is_even_sub(x))
