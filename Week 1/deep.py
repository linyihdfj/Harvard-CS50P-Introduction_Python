number = input("What's the answer to the Great Question of Life, the Universe and Everything\n")

match number:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")