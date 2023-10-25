# Code created by Pepijn Weitzel

def main():
    # Prompt user for the greet
    greet = input("Greet: ").lower()
    money = value(greet)
    print(f"${money}")

def value(greeting):
    # Check whether greet = hello or start with an H
    if "hello" in greeting:
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()