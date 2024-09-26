import emoji

def main():
    emojis = input("Input: ")
    new_emojis = emoji.emojize(emojis, language='alias')
    print("Output: ", new_emojis)

main()
