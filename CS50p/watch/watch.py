# Code created by Pepijn Weitzel

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    if link := re.search(r'^<iframe(?:.)+src="(https?://(?:www\.)?youtube\.com)/embed(/.+)"></iframe>$', s):
        # If string contains https
        if re.search(r".+https.+", s):
            # Change youtube.com to youtu.be
            new_youtube = re.sub(r"youtube\.com", "youtu.be", link.group(1))
            # Get rid of possible www.
            new_youtube = re.sub(r"www\.", "", new_youtube)
            # Give link without /embed
            youtube_link = new_youtube + link.group(2)
            return youtube_link
        # If string contains http
        else:
            # Change http to https
            new_string = re.sub(r"http", "https", link.group(1))
            # Change youtube.com to youtu.be
            new_youtube = re.sub(r"youtube\.com", "youtu.be", new_string)
            # Get rid of possible www.
            new_youtube = re.sub(r"www\.", "", new_youtube)
            # Give link without /embed
            youtube_link = new_youtube + link.group(2)
            return youtube_link

    else:
        return "None"


if __name__ == "__main__":
    main()
