# Code created by Pepijn Weitzel

import random


def main():
    level = get_level()


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        else:
            if level in range(1, 4):
                return level
            else:
                continue


def generate_integer(level):
    if level == 1:
        


if __name__ == "__main__":
    main()