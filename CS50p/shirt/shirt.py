# Code created by Pepijn Weitzel
import sys
from PIL import Image, ImageOps


# Check for errors
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif sys.argv[2][len(sys.argv[2])-5:] != ".jpeg" and sys.argv[2][len(sys.argv[2])-4:] != ".jpg" and sys.argv[2][len(sys.argv[2])-4:] != ".png":
    sys.exit("Invalid output")
elif sys.argv[1][len(sys.argv[1])-4:] != sys.argv[2][len(sys.argv[2])-4:]:
    sys.exit("Input and output have different extensions")

# Open and save images
images = []
try:
    image = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")
else:
    images.append(image)
    shirt = Image.open("shirt.png")

# Size
image_size = image.size
image = ImageOps.fit(image, image_size)

image.paste(shirt, shirt)

image.save(sys.argv[2], save=True)
