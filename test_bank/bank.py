def main():
    greeting = input("Greet me: ")
    if value(greeting) == 0:
        print("$0")
    elif value(greeting) == 20:
        print("$20")
    else:
        print("$100")


def value(greeting):
    greeting = greeting.lower().strip()
    if greeting[:5] == "hello":
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100




if __name__ == "__main__":
    main()

