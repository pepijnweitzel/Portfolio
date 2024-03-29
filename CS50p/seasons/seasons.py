# Code created by Pepijn Weitzel

import datetime
import re
import sys
import inflect

p = inflect.engine()


def main():
    # Get users birthdate
    birth_date = get_date()

    # Get difference with today
    minute_difference = get_difference(birth_date)

    # Change minutes to text
    text = get_text(minute_difference)

    # Print the text
    print(text)


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


def get_difference(birthdate):

    current_date = datetime.date.today()
    return ((current_date - birthdate).days) * 24 * 60


def get_text(minutes):
    text = p.number_to_words(minutes, andword="")
    text += " minutes"
    return text.capitalize()

if __name__ == "__main__":
    main()
