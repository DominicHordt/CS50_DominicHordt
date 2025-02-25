def main():
    time = input("What time is it? ")
    conv = convert(time)
    if conv >= 7 and conv <= 8:
        print("breakfast time")
    elif conv >= 12 and conv <= 13:
        print("lunch time")
    elif conv >= 18 and conv <= 19:
        print("dinner time")


def convert(time):
    if "12" in time and "a.m." in time:
        time = time.replace("12", "0").removesuffix(" a.m.")
    elif "a.m." in time:
        time = time.removesuffix(" a.m.")
    elif "12" in time and "p.m." in time:
        time = time.removesuffix(" p.m.")
    elif "p.m." in time:
        time = time.removesuffix(" p.m.")
        x = int((time.split(":"))[0])
        time = time.replace(str(x), str(x+12))

    h, m = float((time.split(":"))[0]), float((time.split(":"))[1])
    m = m/60
    return h+m



if __name__ == "__main__":
    main()
