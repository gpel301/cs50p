import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) > 2:
        file = sys.argv[1]
        new_file = sys.argv[2]
        if not file.endswith(".csv") and not new_file.endswith(".csv"):
            sys.exit("Not a CSV file")
        else:
            try:
                with open (file, "r") as names, open (new_file, "w") as new_names:
                    reader = csv.DictReader(names)
                    writer = csv.DictWriter(new_names, fieldnames = ["first", "last", "house"])
                    writer.writeheader()

                    for row in reader:
                        last, first = row["name"].split(",")
                        last = last.strip()
                        first = first.strip()shirt
                        house = row["house"]
                        writer.writerow({"first": first, "last": last, "house": house})


            except FileNotFoundError:
                sys.exit(f"Could not read {file}")

main()
