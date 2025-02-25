coke_cost = 50
amount = 0
while amount < coke_cost:
    insert = 0
    while not (insert == 25 or insert == 10 or insert == 5):
        print(f"Amount Due: {coke_cost - amount}")
        insert = int(input("Insert Coin: "))
    amount += insert
print(f"Change Owed: {amount - coke_cost}")
