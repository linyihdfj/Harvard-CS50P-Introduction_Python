import sys
import requests

total = 0

if len(sys.argv) == 1:
    print("Missing command-line argument")
    sys.exit(1)

try:
    total = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

r = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=f885e93bf934f1e0388aaf0ddcaf65aa317fd0b77b2f730d6d36868fcb933569")
data = r.json()
price = float(data["data"]["priceUsd"])
print(f"${total * price:,.4f}")