# Code created by Pepijn Weitzel
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    if time := re.search(r"((?:[0-9](?::[0-5][0-9])?)|(?:1[0-2])(?::[0-5][0-9])?) ((?:AM)|(?:PM)) to ((?:[0-9](?::[0-5][0-9])?)|(?:1[0-2])(?::[0-5][0-9])?) ((?:AM)|(?:PM))", s):
        # Check for which format was used
        if ":" in time.group(1):
            hours, minutes = time.group(1).split(":")
            if time.group(2) == "PM":
                if hours != "12":
                    hours = str(int(hours) + 12)
                else:
                    hours = "12"
            else:
                if hours == "12":
                    hours = "00"
                elif 0 <= int(hours) <= 9:
                    hours = "0" + hours
            start = f"{hours}:{minutes}"
        else:
            if time.group(2) == "PM":
                start = f"{str(int(time.group(1)) + 12)}:00"
            else:
                start = f"{time.group(1)}:00"

        if ":" in time.group(3):
            hours, minutes = time.group(3).split(":")
            if time.group(4) == "PM":
                if hours != "12":
                    hours = str(int(hours) + 12)
                else:
                    hours = "12"
            else:
                if hours == "12":
                    hours = "00"
                elif 0 <= int(hours) <= 9:
                    hours = "0" + hours
            end = f"{hours}:{minutes}"
        else:
            if time.group(4) == "PM":
                end = f"{str(int(time.group(3)) + 12)}:00"
            else:
                end = f"{time.group(3)}:00"

        return f"{start} to {end}"
    else:
        raise ValueError




if __name__ == "__main__":
    main()
