# Code created by Pepijn Weitzel

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check whether length is right
    if 2 <= len(s) <= 6:
        # Check whether first 2 chars are letters
        if s[0].isalpha() and s[1].isalpha():
            # Check whether no letters after numbers
            first_number = 0
            for i in range(len(s)):
                if s[i].isalpha() == False:
                    first_number = i
                    break
            for i in range(i, len(s)):
                if s[i].isalpha() == True:
                    return False
            # Check for periods, spaces or punctuation
            for char in s:
                if char.isalpha() == False or char.isnum() == False:
                    return False
            return True



    return False

main()