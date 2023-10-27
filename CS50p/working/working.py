# Code created by Pepijn Weitzel
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    if time := re.search(r"((?:[0-9](?::[0-5][0-9])?)|(?:1[0-2])(?::[0-5][0-9])?) ((?:AM)|(?:PM)) to ((?:[0-9](?::[0-5][0-9])?)|(?:1[0-2])(?::[0-5][0-9])?) ((?:AM)|(?:PM))", s):
        # Check for which format was used
        if ":" in time.group(1):
            hours, minutes = time.group(1).split(":")
            

        return start
    else:
        raise ValueError




if __name__ == "__main__":
    main()
