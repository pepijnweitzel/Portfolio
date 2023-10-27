# Code created by Pepijn Weitzel

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if link := re.search(r'<iframe(?:.)+src"', s)


if __name__ == "__main__":
    main()
