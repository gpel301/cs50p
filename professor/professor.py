import random


def main():
    # result_list: []
    score = 0
    level = get_level()
    count = 0
    while count != 10:
        question = ask_question(level)
        count += 1
        if question == 1:
            score += 1

    print("Score: ", score)





    # x = generate_integer(level)
    # y = generate_integer(level)
    # while result_list.index(result) != 10:
    #     result = input(f"{x} + {y} = ")
    #     if result != x + y:
    #         print("EEE")
    #         if result != x + y:
    #             print("EEE")
    #             if result != x + y:
    #                 print("EEE")
    #                 print(f"{x} + {y} = {x + y}")
    #                 result_list.append("x")
    #                 continue


    #     else:
    #         result_list.append(result)
    #         continue

    # print("Scrore: ", result_list.index(result))






        # print(f"{x} + {y}")

    # print("Score: ", number_right)
    # break


   #while True:
        # try:
        #     n = int(input("Level: "))
        #     if n >= 0 or n <= 3:
        #         return get_level(n)
        #     else:
        #         print("EEE")
        #         continue


        # except ValueError:
        #     print("EEE")
        #     continue


def get_level(): #prompt and re-prompt for level and returns 1, 2or 3
    while True:
        try:
            n = int(input("Level: "))
            if n >= 1 and n <= 3:
                return n
            else:
                continue


        except ValueError:
            continue

## if xx raise ValueError

def generate_integer(level): #randomly generated non-negative int with level digits or value error if level not 1, 2 or 3
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


def ask_question(level):

    x = generate_integer(level)
    y = generate_integer(level)
    count = 0
    while count != 3:
        try:
            result = int(input(f"{x} + {y} = "))
            if result != x + y:
                print("EEE")
                count += 1

            else:
                return 1
        except ValueError:
                print("EEE")
                count +=1


    print(f"{x} + {y} = {x + y}")
    return 0





    #     try:
    #     if level == 1:
    #         x = random.randint(0, 9)
    #         y = random.randint(0, 9)
    #         return x and y
    #         # z = int(input(f"{x} + {y} = "))
    #         # if x + y == z:
    #         #     continue
    #         # else:
    #         #     print("EEE")

    #     elif level == 2:
    #         x = random.randint(10, 99)
    #         y = random.randint(10, 99)
    #         # z = int(input(f"{x} + {y} = "))
    #         # if x + y == z:
    #         #     continue
    #         # else:
    #         #     print("EEE")

    #     else:
    #         x = random.randint(100, 999)
    #         y = random.randint(100, 999)
    #         # z = int(input(f"{x} + {y} = "))
    #         # if x + y == z:
    #         #     continue
    #         # else:
    #         #     print("EEE")

    # except ValueError: ## raise value error
    #     print("EEE")
    #     continue


            #ask again for same problem (2 more times max)


if __name__ == "__main__":
    main()
