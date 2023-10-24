# Code created by Pepijn Weitzel

groceries = {}

while True:
    try:
        grocery = input().upper()
        if grocery in groceries:
            groceries[grocery] += 1
        else:
            groceries[grocery] = 1
    except EOFError:
        groceries_keys = sorted(list(groceries.keys()))
        sorted_groceries = {}
        for item in groceries_keys:
            sorted_groceries[item] = groceries[item]
            print(item, sorted_groceries[item])
        break
