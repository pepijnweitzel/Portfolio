# Code created by Pepijn Weitzel

def main():
    while True:
        # Prompt user for fraction
        fraction = input("Fraction: ")
        answer = convert(fraction)

def convert(fraction):
    # Find out how many numbers before /
        j = 0
        for i in range(len(fraction)):
            if fraction[i] == "/":
                index = i
                j = 1

        # Make sure / symbol was given
        if j != 1:
            continue

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
            if z <= 1:
                print("E")
                break
            elif z >= 99:
                print("F")
                break
            else:
                print(f"{z}%")
                break

def gauge(percentage):
    ...


if __name__ == "__main__":
    main()
