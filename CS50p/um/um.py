# Code created by Pepijn Weitzel

import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    if string := re.search(r"^(um[,\.?!\s])?(\sum[\s,.!?\n])", s, re.IGNORECASE):
        print(string.group(1))
        print(string.group(2))
        for char in string.group(2):
            if char.lower() == "u":
                count += 1

    return count


if __name__ == "__main__":
    main()
