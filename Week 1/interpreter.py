expression = input("Expression: ")

x,y,z = expression.split(" ")

x = int(x)
z = int(z)

result = 0
match y:
    case "+":
        result = x + z
    case "-":
        result = x - z
    case "*":
        result = x * z
    case "/":
        result = x / z
print(f"{result:.1f}")