# Code created by Pepijn Weitzel

groceries = {}

while True:
    try:
        grocery = input().upper()
    except EOFError:
        print