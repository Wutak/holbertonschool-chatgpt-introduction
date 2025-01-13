#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        raise ValueError("Lenombre doit Ãtre un entier non nÃgatif.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__name__":
    try:
        n = int(sys.argv[1])
        print(factorial(n))
    except (IndexError , ValueError):
        print("Usage : python3 script.py <entier_non_nÃgatif>")
