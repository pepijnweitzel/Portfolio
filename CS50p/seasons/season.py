# Code created by Pepijn Weitzel

import datetime
import re
import sys


def main():
    given_date = get_date()
    print(given_date)


def get_date():

    string = input("Date of Birth: ")
    if string:= re.search(r"^([0-9]{4})-([0-9]{2})-([0-9]{2})$", string):
        try:
            given_date = datetime.date(int(string.group(1)), int(string.group(2)), int(string.group(3)))
        except ValueError:
            sys.exit("Invalid date")
        else:
            return given_date
    sys.exit("Invalid date")


if __name__ == "__main__":
    main()
