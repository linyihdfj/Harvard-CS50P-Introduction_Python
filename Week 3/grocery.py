grocery_list : dict = {}
while True:
    try:
        grocery = input("")
        if not grocery_list.get(grocery):
            grocery_list.setdefault(grocery, 1)
        else:
            grocery_list[grocery] += 1
    except EOFError:
        break
grocery_list = dict(sorted(grocery_list.items()))
for item, quantity in grocery_list.items():
    print(f"{quantity} {item.upper()}")