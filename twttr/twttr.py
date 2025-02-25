string = input("Input: ")
vowels = ["a", "e", "i", "o", "u"]
new_string = ""

for letter in string:
    if letter.lower() not in vowels:
        new_string += letter
print(f"Output: {new_string}")

