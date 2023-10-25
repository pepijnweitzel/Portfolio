# Code created by Pepijn Weitzel
import requests
import sys
import json

def main():
    # Check for right input
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        number = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    print(response)


if __name__ == "__main__":
    main()