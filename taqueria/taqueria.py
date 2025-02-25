taq_prices = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = int()
while True:
    try:
        item = input("Item: ").title()
    except EOFError:
        break
    if item == "":
        break
    try:
        total = total + taq_prices[item]
        print(f"${total:.2f}")
    except KeyError:
        pass


