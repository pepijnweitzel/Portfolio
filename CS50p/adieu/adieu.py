# Code created by Pepijn Weitzel

def main():
    names = []
    while True:
        try:
            given_name = input("Name: ")
            names.append(given_name)
        except EOFError:
            break

    number_of_people = len(names)
    for 





if __name__ == "__main__":
    main()