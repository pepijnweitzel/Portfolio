# Code created by Pepijn Weitzel

import random


def main():
    level = get_level()
    correct_answers = 0
    for i in range(10):
        correct_answers += question(generate_integer(level), generate_integer(level))
    print(f"Score: {correct_answers}")



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
    # return 1 if answer correct, return 0 if answer incorrect
    incorrect = 0
    z = x + y
    while incorrect < 3:
        try:
            answer = int(input(f"{x} + {y} = "))
        except ValueError:
            incorrect += 1
            print("EEE")
            continue
        else:
            if answer != z:
                incorrect += 1
                print("EEE")
            else:
                # Answer is correct so give point
                return 1
    # If while loop finishes, so 3 mistakes have been made
    return 0


if __name__ == "__main__":
    main()