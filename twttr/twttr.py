def main():
    word = input("Input: ")
    print("Output: ", shorten(word))

def shorten(word):
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    for vowel in vowels:
        word = word.replace(vowel, "")
    return word

if __name__ == "__main__":
    main()

