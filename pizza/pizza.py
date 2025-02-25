import sys
import csv
from tabulate import tabulate

menu = []

if len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
else:
    if sys.argv[1].endswith(".csv"):
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                headers = reader.fieldnames
                for line in reader:
                    menu.append({headers[0]: line[headers[0]], headers[1]: line[headers[1]], headers[2]: line[headers[2]]})
                print(tabulate(menu, headers="keys", tablefmt="grid"))

        except FileNotFoundError:
            sys.exit("File does not exist")
    else:
        sys.exit("Not a CSV file")
