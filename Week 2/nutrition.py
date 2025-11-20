nutrition = {
    "apple": {
        "calories": 130,
    },
    "banana": {
        "calories": 110,
    },
    "orange": {
        "calories": 80,
    },
}
item = input("Item: ").lower()
if item in nutrition:
    print("Calories:", nutrition[item]["calories"])

#I don't want to copy all the items into the dictionary manually