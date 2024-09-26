def main():
    while True:
        try:
            fraction = convert(input("Fraction: "))
            print(gauge(fraction))
            break

        except ValueError:
            continue
        except ZeroDivisionError:
            continue



def convert(fraction):
    x, y = fraction.split("/")
    
    if not x.isdigit() and not y.isdigit() and not y >= x:
            raise ValueError
    elif y == 0:
            raise ZeroDivisionError
    # elif not y >= x:
    #         raise ValueError
    elif not (int(x)/int(y)) * 100 <= 100:
            raise ValueError
    else:
        x = int(x)
        y = int(y)
        fraction = round((x/y) * 100)
        return fraction
        # except ZeroDivisionError:
            # pass
        # except ValueError:
            # pass

    # if x != int(x) or y != int(y):
    #     raise ValueError
    # elif y == 0:
    #     raise ZeroDivisionError
    # elif y > x:
    #     raise ValueError
    # elif not (x/y) * 100 <= 100:
    #     raise ValueError
    # else:

    #     fraction = int(round((x/y) * 100))
    #     return fraction





def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"




if __name__ == "__main__":
    main()
