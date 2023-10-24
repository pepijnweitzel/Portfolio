# Code created by Pepijn Weitzel
# Prompt user for the greet
greet = input("Greet: ").lower()
# Check whether greet = hello or start with an H
if "hello" in greet:
    print("$0")
elif greet[0] == "h":
    print("$20")
else:
    print("$100")