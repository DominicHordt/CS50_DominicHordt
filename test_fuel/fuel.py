def convert():
    while True:
        try:
            (a,b) = (int(z) for z in input("Fraction: ").split("/"))
            if a>b:
                pass
            else:
                return a, b
        except ValueError:
            pass

def gauge(a, b):
    try:
        per = (a / b) * 100
        if per > 100:
            pass
        elif per >= 99:
            return "F"
        elif per <= 1:
            return "E"
        else:
            return f"{round(per)}%"
    except ZeroDivisionError:
        pass

def main():
    x,y = convert()
    print(gauge(x,y))

if __name__ == "__main__":
    main()
