# Code created by Pepijn Weitzel
import sys

# Check for correct input
length = len(sys.argv)
if length < 2:
    sys.exit("Too few command-line arguments")
elif length > 2:
    sys.exit("Too many command-line arguments")
last_characters = sys.argv[1][len(sys.argv[1]) - 3] + sys.argv[1][len(sys.argv[1]) - 2] + sys.argv[1][len(sys.argv[1]) - 1]
if last_characters != ".py":
    sys.exit("Not a Python file")
try:
    file = open(sys.argv[1])
    file.close()
except FileNotFoundError:
    sys.exit("File does not exist")

lines_of_code = []
with open(sys.argv[1]) as file:
    for line in file:
        if len(line) > 0 and len(line.lstrip()) > 0:
            if line.lstrip()[0] != "#":
                lines_of_code.append(line)

print(len(lines_of_code))
