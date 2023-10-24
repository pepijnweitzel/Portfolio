# Code created by Pepijn Weitzel
# Prompt user for answer
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# Check whether answer is correct
match answer:
    case "42" | "forty-two" | "Forty Two":
        print("Yes")
    case _:
        print("No")
