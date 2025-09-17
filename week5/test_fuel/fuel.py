def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)

    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    # Turn the fraction into percent
    fraction = round((x / y * 100))

    if x > y:
        raise ValueError()
    if y == 0:
        raise ZeroDivisionError()

    return fraction


def gauge(percentage):
    # Print the correct values
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%" 


if __name__ == "__main__":
    main()
