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

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    except requests.RequestException:
        sys.exit("Request error")
    else:
        amount = float(response["bpi"]["USD"]["rate_float"])
        amount *= number
        print(f"${amount:,.4f}")

if __name__ == "__main__":
    main()