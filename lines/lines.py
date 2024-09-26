import sys


def main():



    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) > 1:
        file = sys.argv[1]
        if not file.endswith(".py"):
            sys.exit("Not a Python file")
        else:
            try:
                with open(file, "r") as code:
                    count = 0
                    for line in code.readlines():
                        line = line.strip()
                        if not line.startswith("#") and len(line) != 0 :
                            count += 1
                    print(count)

            except FileNotFoundError:
                sys.exit("File does not exist")





main()
