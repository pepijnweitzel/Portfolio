# Code created by Pepijn Weitzel
def main():
    time = input("What time is it? ")
    convert(time)


def convert(time):
    if len(time == 4):
        tmp = len[0]
        minutes = str((float(len[2] + len[3]))/60)
        tmp += minutes
        if 7.00 <= tmp <= 8.00:
            print("breakfast time")
    else:
        tmp = len[0] + len[1]
        minutes = str((float(len[3] + len[4]))/60)
        tmp += minutes
        if 12.00 <= tmp <= 13.00:
            print("lunch time")
        elif 18.00 <= tmp <= 19.00:
            print("dinner time")



if __name__ == "__main__":
    main()