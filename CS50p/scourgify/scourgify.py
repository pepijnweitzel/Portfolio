# Code created by Pepijn Weitzel
import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
try:
    file = open(sys.argv[1])
    file.close()
except FileNotFoundError:
    sys.exit("Could not read ", sys.argv[1])


students = []
with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(row)

new_students = []
for student in students:
    studen = {}
    last_name, first_name = student["name"].split(",")
    studen["first"] = first_name
    studen["last"] = last_name
    studen["house"] = student["house"]
    new_students.append(studen)


with open(sys.argv[2], "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for student in new_students:
        writer.writerow(student)
