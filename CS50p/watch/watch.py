# Code created by Pepijn Weitzel

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    if link := re.search(r'^<iframe(?:.)+src="(https?://(?:www\.)?youtube\.com)/embed(/.+)"></iframe>$', s):
        youtube_link = link.group(1) + link.group(2)
        return youtube_link
    else:
        return "None"


if __name__ == "__main__":
    main()
