while True:
    try:
        x,y = map(int,input("Fraction: ").split('/'))
        res = x / y
        if x < 0 or y < 0 or res > 1:
            raise ValueError
        if res < 0.01:
            print("E")
        elif res > 0.99:
            print("F")
        else:
            print(f"{round(res*100)}%")
        break
    except (ValueError, ZeroDivisionError):
        pass