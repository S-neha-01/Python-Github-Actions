#!/usr/bin/env python3
"""
Simple Python application that calculates the factorial of a given number.
"""

from factorial import factorial

def main():
    """
    Main function to run the application.
    """
    import sys
    if len(sys.argv) != 2:
        print("Usage: python main.py <number>")
        sys.exit(1)
    try:
        num = int(sys.argv[1])
        result = factorial(num)
        print(f"The factorial of {num} is {result}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()