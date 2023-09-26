from cs50 import get_float

def main():
    change = get_change()
    quarters = int(change / 0.25)
    change = change - quarters * 0.25
    print(str(change) + "na quarters")
    dimes = int(change / 0.10)
    change = change - dimes * 0.10
    print(str(change) + "na quarters")
    nickels = int(change / 0.05)
    change = change - nickels * 0.05
    print(str(change) + "na quarters")
    pennies = int(change / 0.01)

    total_number = quarters + dimes + nickels + pennies
    print(f"{total_number}")




def get_change():
    while True:
        n = get_float("Change owed: ")
        if n > 0:
            return n




main()