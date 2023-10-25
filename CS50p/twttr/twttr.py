# Code created by Pepijn Weitzel

def main():
    text = input("Input: ")
    text = shorten(text)
    print(f"Output: {text}")

def shorten(string):
    new_text = ""
    for letter in string:
        if letter.lower() == "a" or letter.lower() == "e" or letter.lower() == "i" or letter.lower() == "o" or letter.lower() == "u":
            continue
        else:
            new_text += letter
    return new_text
