def main():
    item_list = {}
    try:
        while True:
            item = input().upper()
            if item in item_list:
                item_list[item] += 1
            else:
                item_list[item] = 1


    except EOFError:
        for key in sorted(item_list):
            print(item_list[key], key.upper())


main()
