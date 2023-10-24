# Code created by Pepijn Weitzel

expression = input("Expression: ")

expression = expression.split()

x = expression[0]
y = expression[1]
z = expression[2]

if y == "+":
    print(float(x + z))
elif y == "-":
    print(float(x - z))
elif y == "*":
    print(float(x * z))
elif y == "/":
    print(float(x / z))