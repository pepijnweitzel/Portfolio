# Code created by Pepijn Weitzel
import random


def main():
    level = -1
    while level < 0:
        try:
            level = int(input("Level: "))
            break
        except ValueError:
            continue
    print(level)


if __name__ == "__main__":
    main()