import inflect

p = inflect.engine()

lst = []
while True:
    try:
        i = input("Name: ")
        lst.append(i)
    except EOFError:
        break

print("Adieu, adieu, to " + p.join(lst))
