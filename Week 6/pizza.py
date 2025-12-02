import csv
import tabulate
import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")


path = sys.argv[1]

try:
    file = open(path)
    dictreader = csv.DictReader(file)
    tables = []
    headers = ["Sicilian Pizza", "Small", "Large"]
    for row in dictreader:
        tables.append([row["Sicilian Pizza"], row["Small"], row["Large"]])
    print(tabulate.tabulate(tables, headers, tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")