def value(greeting):
    if greeting.lower().strip().startswith("hello"):
        return("$0")
    elif greeting.lower().strip().startswith("h"):
        return("$20")
    else:
        return("$100")

def main():
    greeting = input("Greeting: ")
    print(value(greeting))

if __name__ == "__main__":
    main()
