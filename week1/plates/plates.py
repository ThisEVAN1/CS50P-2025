def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # If the plate has less than 2 letters or more than 6 characters return false
    if not (6 >= len(s) >= 2):
        return False

    # Return false if plate does not start with 2 letters
    if s[0].isdigit() or s[1].isdigit():
        return False

    # If there is a letter after there a number then return false
    number_present = False
    for c in s:
        if c.isdigit():
            number_present = True
        if number_present and c.isdigit() == False:
            return False

    # If the first number is a 0 return false
    for c in s:
        if c.isdigit() == False:
            continue
        else:
            if c == '0':
                return False
            else:
                break

    # If the plate has periods, spaces, or punctuation marks return false
    for c in s:
        if c == '.' or c == ' ' or c == '?' or c == '!':
            return False

    return True

main()
