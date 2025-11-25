import inflect

names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break

p = inflect.engine()
print(f"Adieu, adieu, to {p.join(names)}")