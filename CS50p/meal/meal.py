# Code created by Pepijn Weitzel
def main():
    time = input("What time is it? ")
    convert(time)


def convert(time):
    if len(time) == 4:
        hour = time[0] + "."
        minutes = str(int(time[2] + time[3])/60*100)
        print(hour + minutes)


if __name__ == "__main__":
    main()