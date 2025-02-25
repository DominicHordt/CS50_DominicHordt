import re


def main():
    print(count(input("Text: ")))


def count(s):
    if matches := re.findall(r"(\sum\W)|(^um\W)|(^um$)", s, re.IGNORECASE):
        return len(matches)
    return 0

if __name__ == "__main__":
    main()
