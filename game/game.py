import random

while True:
    try:
        lvl = int(input("Level: "))
        if lvl < 1:
            pass
        else:
            break
    except ValueError:
        pass

guess = random.randrange(1, lvl)

while True:
    try:
        trial = int(input("Guess: "))
        if trial < guess:
            print("Too small!")
        elif trial > guess:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
