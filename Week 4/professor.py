import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        if ask_question(level):
            score += 1
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

def ask_question(level):
    num1 = generate_integer(level)
    num2 = generate_integer(level)
    for _ in range(3):
        try:
            answer = int(input(f"{num1} + {num2} = "))
            if answer == num1 + num2:
                return True
        except ValueError:
            continue
    print("EEE")
    print(f"{num1} + {num2} = {num1 + num2}")
    return False

if __name__ == "__main__":
    main()
