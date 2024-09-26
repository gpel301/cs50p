def main():
    level = get_frac("Fraction: ")
    if level <= 1:
        print("E")
    elif  level >= 99:
        print("F")
    else:
        print(f"{level}%")


def get_frac(frac):
    while True:
        try:
            x, y = input(frac).split("/")
            x = int(x)
            y = int(y)
            if (x / y) * 100 <= 100:
                return round((x / y) * 100)
            else:
                pass
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()
