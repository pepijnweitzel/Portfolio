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
            # Check whether no letters after numbers and first number == 0
            if no_letters_after_numbers(s):
                # Check for punctuation
                if "." in s or "," in s or "!" in s or " " in s or "!" in s:
                    return False
                return True
    return False

def no_letters_after_numbers(s):
    # Create function that checks if there is a number in plate no letters come after it
    numbers_in_plate = "no"
    for i in range(len(s)):
        if s[i].isnumeric():
            number_index = i
            numbers_in_plate = "yes"
            if s[i] == "0":
                return False
            break
    if numbers_in_plate == "yes":
        for i in range(number_index + 1, len(s)):
            if s[i].isalpha():
                return False
    return True

if __name__ == "__main__":
    main()