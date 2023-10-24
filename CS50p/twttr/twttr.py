# Code created by Pepijn Weitzel
text = input("Input: ")
new_text = ""
for letter in text:
    if letter.lower() == "a" or letter.lower() == "e" or letter.lower() == "i" or letter.lower() == "o" or letter.lower() == "u":
        continue
    else:
        new_text += letter
print(f"Output: {new_text}")