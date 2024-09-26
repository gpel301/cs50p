def main():
    greeting = input("Greet me: ")
    if greeting_hello(greeting):
        print("$0")
    elif greeting_h(greeting):
        print("$20")
    else:
        print("$100")


def greeting_hello(x):
    x = x.lower().strip()
    return True if x[:5] == "hello" else False


def greeting_h(y):
    y = y.lower().strip()
    return True if y[0] == "h" else False

main()

