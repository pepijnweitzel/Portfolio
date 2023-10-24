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
        info = date.split("/")
        

    # Check which format it has used
    elif len(date.split()) == 3:
        info = date.split()


    break