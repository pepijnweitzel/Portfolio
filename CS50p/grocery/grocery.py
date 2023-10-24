# Code created by Pepijn Weitzel

groceries = {}

while True:
    try:
        grocery = input().upper()
    except EOFError:
        for item in groceries:
            print()