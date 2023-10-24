# Code created by Pepijn Weitzel

camel_case = input("camelCase: ")

snake_case = ""
for letter in camel_case:
    if letter.isupper():
        letter = "_" + letter.lower()
    snake_case += letter
print(f"snake_case: {snake_case}")