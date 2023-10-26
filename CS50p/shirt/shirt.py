# Code created by Pepijn Weitzel
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][len(sys.argv[1])-5] != ".jpeg" or sys.argv[1][len(sys.argv[1])-4] != ".jpg" or sys.argv[1][len(sys.argv[1])-4] != ".png":
    sys.exit("")
