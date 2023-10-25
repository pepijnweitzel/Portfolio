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
    print("")
    for i in range(number_of_people):
        names[i] +=
    print(names)





if __name__ == "__main__":
    main()