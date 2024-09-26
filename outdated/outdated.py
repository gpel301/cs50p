months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        date = input("Date: ").title()
        if "/" in date:
            try:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
                if day <= 31 and month <= 12:
                    print(f"{year}-{month:02}-{day:02}")
                    break
                else:
                    continue
            except ValueError:
                continue

        else:
            month, day, year = date.split(" ")
            if "," not in date:
                continue
            if month not in months:
                continue
            day = day.replace(",", "")
            day = int(day)
            year = int(year)
            if day <= 31:
                    month_new = months.index(month) + 1
                    print(f"{year}-{month_new:02}-{day:02}")
                    break
            else:
                continue




main()
