def main():
    print(gauge(convert(input("Fraction: "))))

def convert(fraction : str):
    try:
        x,y = map(int,fraction.split('/'))
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        res = x / y
        return res

    except ValueError:
        raise ValueError
    
def gauge(percentage):
    result = ""
    if percentage < 0.01:
        result = "E"
    elif percentage > 0.99:
        result = "F"
    else:
        result = f"{round(percentage*100)}%"
    return result

if __name__ == "__main__":
    main()
