from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(figlet.getFonts()))
elif len(sys.argv) == 2:
    print("Invalid usage")
    sys.exit(1)
elif len(sys.argv) == 3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        print("Invalid usage")
        sys.exit(1)
    try:
        figlet.setFont(font=sys.argv[2])
    except Exception:
        print("Invalid usage")
        sys.exit(1)

sentence = input("Input: ")
print("Output:")
print(figlet.renderText(sentence))