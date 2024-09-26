import sys
from tabulate import tabulate
import csv


def main():



    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) > 1:
        file = sys.argv[1]
        if not file.endswith(".csv"):
            sys.exit("Not a CSV file")
        else:
            try:

                with open(file) as menu:
                    reader = csv.reader(menu)

                    print(tabulate(reader, headers = "firstrow", tablefmt = "grid"))



            except FileNotFoundError:
                sys.exit("File does not exist")





main()
