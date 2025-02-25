def main():
    string = input("Input: ")
    print(shorten(string))

def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    new_string = ""
    for letter in word:
        if letter.lower() not in vowels:
            new_string += letter
    return f"Output: {new_string}"


if __name__ == "__main__":
    main()
