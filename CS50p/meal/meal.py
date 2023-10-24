# Code created by Pepijn Weitzel
def main():
    time = input("What time is it? ")
    time = convert(time)
    if 7.00 <= time <= 8.00:
        print("breakfast time")
    elif 12.00 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")

def convert(time):
    if len(time) == 4:
        hour = time[0] + "."
        minutes = str(int(time[2] + time[3])/60*100).split(".")[0]
        return float(hour + minutes)
    else:
        hour = time[0] + time[1] + "."
        minutes = str(int(time[3] + time[4])/60*100).split(".")[0]
        return float(hour + minutes)

if __name__ == "__main__":
    main()