# Code created by Pepijn Weitzel
def main():
    time = input("What time is it? ")
    convert(time)


def convert(time):
    if len(time) == 4:
        tmp = time[0]
        minutes = str((float(time[2] + time[3]))/60)
        tmp += minutes[1] + minutes[2]
        print(tmp)
        if 7.00 <= float(tmp) <= 8.00:
            print("breakfast time")
    else:
        tmp = time[0] + time[1]
        minutes = str((float(time[3] + time[4]))/60)
        tmp += minutes[1] + minutes[2]
        if 12.00 <= float(tmp) <= 13.00:
            print("lunch time")
        elif 18.00 <= float(tmp) <= 19.00:
            print("dinner time")

if __name__ == "__main__":
    main()