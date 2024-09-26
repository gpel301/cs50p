
def main():
    camelCase = input("camelCase: ")
    print("snake_Case: ", snake_case(camelCase))


def snake_case(camelCase):
    result =[]
    for char in camelCase:
        if char.isupper():
            result.append("_")
            result.append(char.lower())
        else:
            result.append(char)
    return "".join(result)


main()
