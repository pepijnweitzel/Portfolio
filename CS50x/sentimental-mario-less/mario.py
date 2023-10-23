def main():
    height = get_height()
    spaties = height
    for i in range(height):
        spaties -= 1
        hashes = i + 1
        print(" " * spaties + "#" * hashes)


def get_height():
    while True:
        try:
            number = int(input("Height: "))
        except ValueError:
            continue
        else:
            if 1 <= number <= 8:
                return number


main()
