# Code created by Pepijn Weitzel

import datetime
import re
import sys


def main():
    birth_date = get_date()
    current_date = datetime.date.today()
    date_difference = current_date - birth_date
    print(type(date_difference))


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
