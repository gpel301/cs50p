def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ##checks if plates length is between 2 and 6
    if len(s) < 2 or len(s) > 6:
        return False
    ##checks if plate starts with at least 2 letters
    for i in range(2):
        if not s[i].isalpha():
            return False
    ## no periods, space, punctuation
    if not s.isalnum():
        return False
    for i in s:
            if i.isdigit():
                result = s.index(i)
                if s[result:].isdigit() and int(i) != 0:
                    return True
                else:
                    return False

    return True



main()



