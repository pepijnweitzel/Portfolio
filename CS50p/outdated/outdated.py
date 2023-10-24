# Code created by Pepijn Weitzel

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    # Get date from user
    date = input("Date: ")

    # Check which format it has used
    if len(date.split("/")) == 3:
        # Get list of all dates
        info = date.split("/")
        # Make all dates integers
        for i in range(len(info)):
            info[i] = int(info[i])
        #Check whether dates are correct
        if info[1] < 0 or info[1] > 31:
            continue
        elif info[0] < 0 or info[1] > 12:
            continue
        else:
            if info[0] < 10:
                info[0] = "0" + str(info[0])
            if info[1] < 10:
                info[1] = "0" + str(info[1])
            print(f"{info[2]}-{info[0]}-{info[1]}")
            break


    # Check which format it has used
    elif len(date.split()) == 3:
        # Get list of all dates
        info = date.split()
        if "," in info[1]:
            info[1] = info[1].strip(",")
        else:
            continue
        if info[0] not in months:
            continue
        if int(info[1]) < 0 or int(info[1]) > 31:
            continue
        else:
            if int(info[1]) < 10:
                info[1] = "0" + info[1]

            info[0] = months.index(info[0]) + 1
            print(f"{info[2]}-{info[0]}-{info[1]}")
            break