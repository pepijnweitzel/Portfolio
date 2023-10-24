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
        for data in info:
            data = int(data)
        # Check whether dates are correct
        if info[1] < 0 or info[1] > 31:
            continue
        if info[0] < 0 or info[1] > 12:
            continue
        print(f"{info[0]}-{info[1]}-{info[2]}")
        break


    # Check which format it has used
    elif len(date.split()) == 3:
        info = date.split()


    break