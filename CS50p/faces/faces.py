# Code created by Pepijn Weitzel
def main():
    # Prompt user for input
    text = input()
    # Print converted text
    print(convert(text))

# Convert :) and :( to smileys
def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

main()