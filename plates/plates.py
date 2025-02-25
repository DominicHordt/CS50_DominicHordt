def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    digits = []
    for i in range(len(s)):
        if s[i].isdigit():
            digits.append(s[i])
        if i!=0:
            if s[i-1].isdigit() and s[i].isalpha():
                return False
                break

    return ((len(s) >2 and len(s) <= 6) and (s.isalpha() or s.isalnum()) and (s[0].isalpha() and s[1].isalpha()) and (digits == [] or digits[0] != "0"))

main()
