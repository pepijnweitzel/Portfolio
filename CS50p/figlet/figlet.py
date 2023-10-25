# Code created by Pepijn Weitzel
from pyfiglet import Figlet
import sys
from random import choice

figlet = Figlet()

all_fonts = figlet.getFonts()

# Check for errors
if len(sys.argv) != 3:
    sys.exit("Invalid usage")
elif sys.argv[2] not in all_fonts:
    sys.exit("Invalid usage")
elif sys.argv[1] != "-f" and sys.argv[1] != "--font":
    sys.exit("Invalid usage")
else:
    set_font = choice(all_fonts)
    figlet.setFont(font=set_font)
    text = input("Input: ")
    print("Output:")
    print(figlet.renderText(text))