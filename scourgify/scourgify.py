import sys
import csv

def main():
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1].endswith(".csv"):
            try:
                with open(sys.argv[1]) as file, open(sys.argv[2], 'w') as new_file:
                    write_new_file(file, new_file)
            except FileNotFoundError:
                sys.exit(f"Could not read " + sys.argv[1])
        else:
            sys.exit("Not a CSV file")

def write_new_file(file, new_file):
    reader = csv.DictReader(file)
    writer = csv.DictWriter(new_file, fieldnames=['first', 'last', 'house'])
    writer.writeheader()
    for line in reader:
        last, first = line['name'].split(', ')
        writer.writerow({'first':first, 'last':last, 'house':line['house']})

if __name__ == "__main__":
    main()
