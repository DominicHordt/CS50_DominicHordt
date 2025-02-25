item_list = []

while True:
    try:
        item = input()
        item_list.append(item)
    except EOFError:
        break
ready_list = set(item_list)
for i in (sorted(ready_list)):
    print(str(item_list.count(i)) + " " + i.upper())
