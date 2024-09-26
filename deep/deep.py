def main():
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything?: ")
    if is_42(answer):
        print("Yes")
    else:
        print("No")

def is_42(x):
    x = x.lower().strip()
    return x == "42" or x == "forty-two" or x == "forty two"





main()
