import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if s.startswith("<iframe"):
        if matches := re.search(r"https?://(www\.)?youtube\.com/embed/\w+", s):
            return re.sub(r"https?://(www\.)?youtube\.com/embed/", "https://youtu.be/", matches.group(0))


if __name__ == "__main__":
    main()
