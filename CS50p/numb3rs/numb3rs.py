# Code created by Pepijn Weitzel
import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if ip_adress := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        if 0 <= int(ip_adress.group(1)) <= 255:
            if 0 <= int(ip_adress.group(2)) <= 255:
                if 0 <= int(ip_adress.group(3)) <= 255:
                    if 0 <= int(ip_adress.group(4)) <= 255:
                        return True
    return False



if __name__ == "__main__":
    main()
