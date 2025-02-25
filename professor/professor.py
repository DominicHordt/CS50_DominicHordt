import random


def main():
    lvl = get_level()
    score = 0
    iter = 0
    while iter < 10:
        x, y = (generate_integer(lvl)), (generate_integer(lvl))
        answer = x + y
        for j in range(3):
            try:
                inpt = int(input(f"{x} + {y} = "))
                if inpt == answer:
                    score += 1
                    break
                elif j == 2 and inpt != answer:
                    print("EEE")
                    print(f"{x} + {y} = {answer}")
                else:
                    print("EEE")
            except ValueError:
                if j == 2:
                    print("EEE")
                    print(f"{x} + {y} = {answer}")
                else:
                    print("EEE")
                    pass
        iter +=1
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                pass
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
