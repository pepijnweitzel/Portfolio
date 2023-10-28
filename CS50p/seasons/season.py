# Code created by Pepijn Weitzel

from datetime import date
import re
import sys


def main():
    given_date = get_date()
    print(given_date)


def get_date():

    string = input("Date of Birth: ")
    if string:= re.search(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})", string):
        if  1 <= int(string.group(2)) <= 12:
            if 1 <= int(string.group(3)) <= 30:

                    return [string.group(1), string.group(2), string.group(3)]
    sys.exit("Invalid date")


if __name__ == "__main__":
    main()
