# Code created by Pepijn Weitzel
# Prompt user for the greet
greet = input("Greet: ").lower().strip().strip(",")
lister = greet.split()
print(lister[0])
# Check whether greet = hello or start with an H
if greet == "hello" or lister[0] == "hello":
    print("$0")
elif greet[0] == "h":
    print("$20")
else:
    print("$100")