def main():
    emoji = input("type a sentence including :) or :( ")
    print(convert(emoji))


def convert(emoji):
   return emoji.replace(":)", "🙂").replace(":(", "🙁")

    




main()
