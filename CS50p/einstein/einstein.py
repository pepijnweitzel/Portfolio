# Code created by Pepijn Weitzel
def main():
    # Prompt user for mass
    mass = int(input("m: "))
    # Make the calculation and print answer
    print(f"E: {joule_calc(mass)}")

# Calculate energy corresponding to given mass
def joule_calc(m):
    e = m * (300000000**2)
    return e

main()