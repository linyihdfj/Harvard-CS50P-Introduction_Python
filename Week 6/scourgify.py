import sys
import csv
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
    
readerPath = sys.argv[1]
writerPath = sys.argv[2]
try:
    reader = csv.DictReader(open(readerPath, "r"))
    writer = csv.DictWriter(open(writerPath, "w", newline=''), fieldnames=["first", "last","house"])
    for row in reader:
        fullName = row["name"].split(" ")
        firstName = fullName[0][0:-1]
        lastName = fullName[1]
        house = row["house"]
        writer.writerow({"first": firstName, "last": lastName, "house": house})
except FileNotFoundError:
    sys.exit(f"File Not Found")