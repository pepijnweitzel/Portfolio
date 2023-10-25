# Code created by Pepijn Weitzel
import requests
import sys

def main():
    # Check for right input
    if sys.argv != 2:
        sys.exit("Missing command-line argument")
    try:
        number = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    


if __name__ == "__main__":
    main()