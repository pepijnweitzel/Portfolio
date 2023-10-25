# Code created by Pepijn Weitzel

import random


def main():
    level = get_level()
    x = generate_integer(level)
    y = generate_integer(level)



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
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(0, 99)
    elif level == 3:
        return random.randint(0, 999)
    else:
        raise ValueError

def question(x, y):
    z = x + y
    

if __name__ == "__main__":
    main()