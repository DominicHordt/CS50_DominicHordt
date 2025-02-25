from datetime import date
import sys
import re
import inflect


def main():
    print(print_date(count_date(input_date(input("Date of Birth: ")))))


def input_date(birth_date):
    matches = re.search(r"^(\d{4})-(\d{2})-(\d{2})$", birth_date)
    if not matches:
        sys.exit("Invalid date")
    else:
        return date(int(matches.group(1)), int(matches.group(2)), int(matches.group(3)))

def count_date(datum):
    today = date.today()
    return int((today - datum).days)*24*60

def print_date(datum):
    p = inflect.engine()
    return (f"{p.number_to_words(datum)} minutes".capitalize().replace(" and", ""))


if __name__ == "__main__":
    main()
