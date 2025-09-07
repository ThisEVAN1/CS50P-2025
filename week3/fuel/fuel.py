while True:
    try:
        fraction = input('Fraction: ')

        # print(fraction.split('/'))
        x, y = fraction.split('/')
        x = float(x)
        y = float(y)

        # Turn the fraction into percent
        percent = round((x / y * 100))

        # If percent is greater than 100 or less than 0 then raise a ValueError
        if 0 > percent or percent > 100:
            raise ValueError()

        # If percent isn't an int
        if not (x == int(x) and y == int(y)):
            raise ValueError()

    except ValueError:
        print('ValueError')
    except ZeroDivisionError:
        print('ZeroDivisionError')

    else:
        # Print the correct values
        if percent >= 99:
            print('F')
        elif percent <= 1:
            print('E')
        else:
            print(f'{percent}%')

        break
