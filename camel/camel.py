string = input("camelCase: ")
new_string = ""
for character in string:
    if character.isupper():
        new_string = new_string + "_" + character.lower()
    else:
        new_string = new_string + character
print(f"snake_case: {new_string}")
