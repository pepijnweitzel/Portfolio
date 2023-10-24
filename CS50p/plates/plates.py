# Code created by Pepijn Weitzel

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6:
        if s[0].isalpha() and s[1].isaplha():
            return True
    return False

main()