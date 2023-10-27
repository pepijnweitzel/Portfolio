# Code created by Pepijn Weitzel

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    if link := re.search(r'^<iframe(?:.)+src="(https?://(?:www\.)?youtube\.com)/embed(/.+)"></iframe>$', s):
        # If string contains https
        if re.search(r".+https.+", s):
            youtube_link = link.group(1) + link.group(2)
            return youtube_link
        # If string contains http
        else:
            link.group(1) = re.sub(r"http", "https", link.group(1))
            youtube_link = link.group(1) + link.group(2)
            return youtube_link

    else:
        return "None"


if __name__ == "__main__":
    main()
