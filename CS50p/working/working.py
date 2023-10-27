# Code created by Pepijn Weitzel
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    if time := re.search(r"((?:[0-9](?::[0-5][0-9])?)|(?:1[0-2])(?::[0-5][0-9])?) ((?:AM)|(?:PM)) to ((?:[0-9](?::[0-5][0-9])?)|(?:1[0-2])(?::[0-5][0-9])?) ((?:AM)|(?:PM))", s):
        print(time.group(1))
        print(time.group(2))
        print(time.group(3))
        print(time.group(4))
        return time
    else:
        raise ValueError




if __name__ == "__main__":
    main()
