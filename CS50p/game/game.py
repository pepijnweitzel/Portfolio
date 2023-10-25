# Code created by Pepijn Weitzel
import random


def main():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
            else:
                 continue
        except ValueError:
                continue
    # user gave right input:
    number = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
             continue
        else:
             if guess > number:
                  print("Too large!")
                  continue
             elif guess < number:
                  print("Too small!")
                  continue
             else:
                  print("Just right!")
                  break


if __name__ == "__main__":
    main()