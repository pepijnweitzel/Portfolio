from cs50 import get_float

def main():
    change = get_change()
    quarters = int(change / 0.25)
    change = round(change - quarters * 0.25)
    dimes = int(change / 0.10)
    change = round(change - dimes * 0.10)
    nickels = int(change / 0.05)
    change = round(change - nickels * 0.05)
    pennies = int(change / 0.01)

    total_number = quarters + dimes + nickels + pennies
    print(f"{total_number}")




def get_change():
    while True:
        n = get_float("Change owed: ")
        if n > 0:
            return n




main()