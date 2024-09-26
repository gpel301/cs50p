def main():
    expression = input("Expression: ")
    result = float(calc(expression))
    print(round(result, 1))


def calc(n):
    x, y, z = n.split(" ")
    x = int(x)
    z = int(z)


    if y == "+":
        return (x + z)
    elif y == "-":
        return (x - z)
    elif y == "*":
        return (x * z)
    else:
        return (x / z)


main()
