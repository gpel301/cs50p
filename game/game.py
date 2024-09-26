import random

def main():

    while True:
        try:
            n = int(input("Level: "))
            if not n > 0:
                continue
            else:
                random_number = random.randint(1, n)
                guess = int(input("Guess: "))
                if not guess > 0:
                    continue
                elif guess < random_number:
                    print("Too small!")
                elif guess > random_number:
                    print("Too large!")
                elif guess > n:
                    print("Too large!")
                else:
                    print("Just right!")
                    break


        except ValueError:
            continue

main()
