def main():
    greeting = input("Greeting: ").lower().strip()
    print(value(greeting))


def value(greeting):
    result = ""
    if greeting.startswith("hello"):
        result = "$0"
    elif greeting.startswith("h"):
        result = "$20"
    else:
        result = "$100"
    return result

if __name__ == "__main__":
    main()
