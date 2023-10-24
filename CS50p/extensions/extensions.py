# Code created by Pepijn Weitzel
# Prompt user for file name
file = input("File name: ").lower()

match file:
    case str(x) if ".gif" in x:
        print("test")
