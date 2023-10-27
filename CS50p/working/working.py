# Code created by Pepijn Weitzel
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    if time := re.search(r"((?:[0-9](?::[0-5][0-9])?)|(?:1[0-2])(?::[0-5][0-9])?) ((?:AM)|(?:PM)) to ((?:[0-9](?::[0-5][0-9])?)|(?:1[0-2])(?::[0-5][0-9])?) ((?:AM)|(?:PM))", s):
        if time.group(2) == "AM":
            start = time.group(1)
        else:
            start == str(int(time.group(1)) + 12)

        return start
    else:
        raise ValueError




if __name__ == "__main__":
    main()
