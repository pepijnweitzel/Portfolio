# Code created by Pepijn Weitzel
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
try:
    file = open(sys.argv[1])
    file.close()
except FileNotFoundError:
    sys.exit("Could not read ", sys.argv[1])

