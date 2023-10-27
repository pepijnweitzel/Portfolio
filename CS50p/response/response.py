# Code created by Pepijn Weitzel

from validator_collection import validators, errors

def main():
    email = input("What's you email address? ")

    try:
        email = validators.email(email)
    except errors.InvalidEmailError:
        print("Invalid")
    else:
        print("Valid")

if __name__ == "__main__":
    main()
