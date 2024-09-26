def main():
    amount_due = 50
    print("Amount Due:", amount_due)

    while amount_due > 0:
        insert = insert_coin()
        if insert != 0:
            amount_due -= insert
            if amount_due > 0:
                print("Amount Due:", amount_due)
        else:
            print("Amount Due:", amount_due)

    if amount_due <= 0:
        print("Change Owed:", abs(amount_due))

def insert_coin():
    while True:
        n = int(input("Insert Coin:"))
        if n in [5, 10, 25]:
            return n
        else:
            return 0





main()

