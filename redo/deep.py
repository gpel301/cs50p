def main():
    life = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()
    if is_42(life):
        print("Yes")
    else:
        print("No")


def is_42(life):

    if life == "42":
        return True
    elif life == "forty-two":
        return True
    elif life == "forty two":
        return True

    else:
        False

main()
