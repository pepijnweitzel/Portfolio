# Code created by Pepijn Weitzel

expression = input("Expression: ")

expression = expression.split()

x = int(expression[0])
y = expression[1]
z = int(expression[2])

if y == "+":
    print(float(x + z))
elif y == "-":
    print(float(x - z))
elif y == "*":
    print(float(x * z))
elif y == "/":
    print(float(x / z))