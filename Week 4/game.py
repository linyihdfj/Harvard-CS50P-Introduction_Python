import random

while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            continue
        break
    except ValueError:
        continue
secret_number = random.randint(1, level)
while True:
    try:
        guess = int(input("Guess: "))
        if guess < 1:
            continue
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Just right!")
            break
    except ValueError:
        continue