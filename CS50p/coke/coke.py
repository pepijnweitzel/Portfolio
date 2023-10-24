# Code created by Pepijn Weitzel

amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    insertion = int(input("Insert coin: "))
    if insertion == 5 or insertion == 10 or insertion == 25:
        amount_due -= insertion

if amount_due == 0:
    print("Change owed: 0")
else:
    print(f"Change owed: {amount_due * -1}")
