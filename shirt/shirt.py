import sys
from PIL import Image, ImageOps
import os



def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else: #len(sys.argv) > 2:
        file = sys.argv[1].lower()
        new_file = sys.argv[2].lower()
        ext_1 = os.path.splitext(file)
        ext_2 = os.path.splitext(new_file)
        endings = [".jpg", ".jpeg", ".png"]
        if ext_1[1] == "" or ext_2[1] =="":
            sys.exit("Invalid input")
        elif ext_1[1] not in endings or ext_2[1] not in endings:
            sys.exit("Invalid input")
        elif ext_1[1] != ext_2[1]:
            sys.exit("Input and output have different extensions")

        try:
            shirt = Image.open("shirt.png")
            size = shirt.size

            with Image.open(file) as img_in:
                img_fit = ImageOps.fit(img_in, size)
                img_fit.paste(shirt, shirt)
                img_fit.save(new_file)






        except FileNotFoundError:
            sys.exit("File not found")

main()
