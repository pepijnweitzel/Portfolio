# Code created by Pepijn Weitzel

def main():
    while True:
        # Prompt user for fraction
        fraction = input("Fraction: ")
        answer = convert(fraction)
        print(gauge(answer))

def convert(fraction):
    # Find out how many numbers before /
        j = 0
        for i in range(len(fraction)):
            if fraction[i] == "/":
                index = i
                j = 1

        # Make sure / symbol was given
        if j != 1:
            raise ValueError

        # Create x variable
        x = ""
        for i in range(index):
            x += fraction[i]
        # Create y variable
        y = ""
        for i in range(index + 1, len(fraction)):
            y += fraction[i]

        # Make sure x and y are integers
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            raise ValueError

        # Make sure y is bigger than x
        if x > y:
            raise ValueError

        try:
            z = float(x) / float(y)
        except ZeroDivisionError:
            raise ZeroDivisionError
        else:
            z = round(z * 100)
            return z


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
