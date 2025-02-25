x, y, z = input("Expression: ").split(" ")

x = float(x)
z = float(z)

if y == "/" and z == 0:
    print("Cannot divide by zero!")
elif y == "+":
    print(round(x+z, 1))
elif y == "-":
    print(round(x-z, 1))
elif y == "*":
    print(round(x*z, 1))
elif y == "/":
    print(round(x/z, 1))
