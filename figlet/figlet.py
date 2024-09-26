from pyfiglet import Figlet
import sys
import random




def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    f = sys.argv[2]


    if len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Invalid usage")
        elif sys.argv[2] not in fonts:
            sys.exit("Invalid usage")
        else:
            s = input("Input :")
            figlet.setFont(font = f)
            print(f"Output: {figlet.renderText(s)}")


    elif len(sys.argv) == 1:
        s = input("Input :")
        f = random.choice(fonts)
        figlet.setFont(font = f)
        print(f"Output: {figlet.renderText(s)}")

    else:
        sys.exit("Invalid usage")







main()
