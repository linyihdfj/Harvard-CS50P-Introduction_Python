import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
path = sys.argv[1]

try:
    tot = 0
    file = open(path, "r")
    for line in file:
        line = line.lstrip()
        if len(line) > 0 and (not line.startswith("#")):
            tot += 1
    print(tot)
    file.close()
except FileNotFoundError:
    sys.exit(f"File Does Not Exist")