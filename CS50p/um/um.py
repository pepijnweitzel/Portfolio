# Code created by Pepijn Weitzel

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    if string := re.search(r"([\s]um[\s,\.])*", s, re.IGNORECASE):
        print(string.group(1))


    return count


if __name__ == "__main__":
    main()
