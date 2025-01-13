#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculates the factorial of a non-negative integer recursively.

    parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the input number. Returns 1 if m is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n -1)

f = factorial(int(sys.argv[1]))
print(f)
