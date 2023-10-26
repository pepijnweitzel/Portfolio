# Code created by Pepijn Weitzel
import sys
from PIL import Image


# Check for errors
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif sys.argv[2][len(sys.argv[2])-5:] != ".jpeg" or sys.argv[2][len(sys.argv[2])-4:] != ".jpg" or sys.argv[2][len(sys.argv[2])-4:] != ".png":
    print()
    sys.exit("Invalid output")
elif sys.argv[1][len(sys.argv[1])-4:] != sys.argv[2][len(sys.argv[2])-4:]:
    sys.exit("Input and output have different extensions")

# Open and save images
images = []
image = Image.open(sys.argv[1])
images.append(image)
image = Image.open("shirt.png")
images.append(image)
