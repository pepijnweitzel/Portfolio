# Code created by Pepijn Weitzel
import sys
import csv
from tabulate import tabulate

# Check for correct input
length = len(sys.argv)
if length < 2:
    sys.exit("Too few command-line arguments")
elif length > 2:
    sys.exit("Too many command-line arguments")
last_characters = sys.argv[1][len(sys.argv[1]) - 4:]
if last_characters != ".csv":
    sys.exit("Not a CSV file")
try:
    file = open(sys.argv[1])
    file.close()
except FileNotFoundError:
    sys.exit("File does not exist")

my_list = []

with open (sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for row in reader:
        my_list.append(row)

print(tabulate(my_list, headers="keys", tablefmt="grid"))
