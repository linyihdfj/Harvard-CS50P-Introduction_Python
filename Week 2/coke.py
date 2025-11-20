amount = 50
while amount > 0:
    print(f"Amount Due: {amount}")
    coin = int(input("Insert coin: "))
    # don't forget to cast to int
    if coin in [25, 10, 5]:
        amount -= coin
print(f"Change Owed: {abs(amount)}")