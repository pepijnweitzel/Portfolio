# Code created by Pepijn Weitzel
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    if time := re.search(r"([0-9]|)"):
        return time

    raise ValueError




if __name__ == "__main__":
    main()