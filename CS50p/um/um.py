# Code created by Pepijn Weitzel

import re


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    if string := re.findall(r"\sum[\s\.,?]", s, re.IGNORECASE):
        count += len(string)
    if string := re.search(r"(^um[\s,\.?])|(^um$)", s, re.IGNORECASE):
        count += 1


    return count


if __name__ == "__main__":
    main()
