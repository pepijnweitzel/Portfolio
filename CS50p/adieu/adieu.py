# Code created by Pepijn Weitzel


def main():
    names = []
    while True:
        try:
            given_name = input()
            names.append(given_name)
        except EOFError:
            break


    number_of_people = len(names)
    if number_of_people == 1:
        print("Adieu, adieu, to", names[0])
    elif number_of_people == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    else:
        print("Adieu, adieu, to", end=" ")
        for name in names[:number_of_people - 1]:
            print(name + ",", end =" ")
        print("and", names[number_of_people - 1])





if __name__ == "__main__":
    main()