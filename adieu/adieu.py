import inflect


def main():
    p = inflect.engine()
    name_list = []
    try:
        while True:
            name = input("Name: ")
            if name not in name_list:
                name_list.append(name)
            else:
                name_list.append(name)

    except EOFError:
        conv_list = p.join(name_list)
        print(f"Adieu, adieu, to {conv_list}")
        
        # for name in name_list:
        #     print(name, end=" ")






main()
