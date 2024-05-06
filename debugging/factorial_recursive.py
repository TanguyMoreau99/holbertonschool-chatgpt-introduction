#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number using recursion.

    Parameters:
        n (int): The number for which factorial is to be calculated.

    Returns:
        int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Extract the input number from command-line arguments and calculate its factorial
f = factorial(int(sys.argv[1]))

# Print the factorial of the given number
print(f)