from cs50 import get_float

def main():
    change = get_change()
    quarters = int(change / 0.25)
    print(quarters)
    change = change - quarters * 0.25
    dimes = int(change / 0.10)
    print(dimes)
    change = change - dimes * 0.10
    nickels = int(change / 0.05)
    print(nickels)
    change = change - nickels * 0.05
    pennies = int(change / 0.01)
    print(pennies)

    total_number = quarters + dimes + nickels + pennies
    print(f"{total_number}")




def get_change():
    while True:
        n = get_float("Change owed: ")
        if n > 0:
            return n




main()