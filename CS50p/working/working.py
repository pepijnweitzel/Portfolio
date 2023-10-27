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
            if int(hours) < 10:
                hours = "0" + hours
            if time.group(2) == "PM":
                if hours != "12":
                    hours = str(int(hours) + 12)
                else:
                    hours = "12"
            else:
                if hours == "12":
                    hours = "00"
            start = f"{hours}:{minutes}"
        else:
            if time.group(2) == "PM":
                if time.group(1) == "12":
                    start = f"{time.group(1)}:00"
                else:
                    start = f"{str(int(time.group(1)) + 12)}:00"
            else:
                if time.group(1) == "12":
                    start = f"00:00"
                if int(time.group(1)) < 10:
                    start = f"0{time.group(1)}:00"
                else:
                    start = f"{time.group(1)}:00"

        if ":" in time.group(3):
            hours, minutes = time.group(3).split(":")
            if int(hours) < 10:
                hours = "0" + hours
            if time.group(4) == "PM":
                if hours != "12":
                    hours = str(int(hours) + 12)
                else:
                    hours = "12"
            else:
                if hours == "12":
                    hours = "00"
            end = f"{hours}:{minutes}"
        else:
            if time.group(4) == "PM":
                if time.group(3) == "12":
                    end = f"{time.group(3)}:00"
                else:
                    end = f"{str(int(time.group(3)) + 12)}:00"
            else:
                if int(time.group(3)) < 10:
                    end = f"0{time.group(3)}:00"
                else:
                    end = f"{time.group(3)}:00"

        return f"{start} to {end}"
    else:
        raise ValueError




if __name__ == "__main__":
    main()
