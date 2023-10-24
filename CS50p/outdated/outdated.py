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
    date = input("Date: ")
    if len(date.split("/")) == 3:
        info = date.split("/")
    else:
        print(date.split())


    break