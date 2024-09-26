def main():
    expression = input("Expression: ")
    result = calculate(expression)
    print(f"{result:.1f}")



def calculate(expression):
    x, y, z = expression.split(" ")
    x = int(x)
    z = int(z)
    if y == "+":
        return float(x + z)
    elif y == "-":
        return float(x - z)
    elif y == "*":
        return float(x * z)
    elif y == "/":
        return float(x / z)



main()




