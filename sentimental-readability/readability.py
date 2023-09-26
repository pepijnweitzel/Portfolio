from cs50 import get_string


text = get_string("Text: ")

words = text.split(" ")
number_words = len(words)

sentences = 0
for char in text:
    if char == "." or char == "!" or char == "?":
        sentences += 1
S = sentences / number_words * 100

letters = 0
for char in text:
    if char.isalpha():
        letters += 1
L = letters / number_words * 100

grade = 0.0588 * L - 0.296 * S - 15.8
if grade >= 16:
    print(f"Grade 16+")
elif grade < 1:
    print(f"Before Grade 1")
else:
    grade = round(grade)
    print(f"Grade {grade}")


# 0.0588 * L - 0.296 * S - 15.8,
# where L is the average number of letters per 100 words in the text, and
# S is the average number of sentences per 100 words in the text.
