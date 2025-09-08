

months = {
    # month: index_of_month
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}


def main():
    # date_format can be MM/DD/YYYY or MonthName/DD/YYYY
    date_format = None

    while True:
        try:
            date = input('Date: ').strip()

            # Check for invalid input

            # Find the correct format of the date
            if '/' in date:
                date_format = 'MM/DD/YYYY'
            else:
                date_format = 'MonthName/DD/YYYY'

            # Convert the MM/DD/YYYY date format into YYYY-MM-DD format
            if date_format == 'MM/DD/YYYY':
                m, d, y = date.split('/')
                if not date_validity(m, d):
                    raise ValueError('Not a valid date')

                print(f'{y}-{int(m):02}-{int(d):02}')
                break

            # Convert the MonthName/DD/YYYY date format into YYYY-MM-DD format
            if date_format == 'MonthName/DD/YYYY':
                # Check if there is a comma
                if date.find(',') == -1:
                    raise Exception('No comma')

                # Remove the comma
                date = date.replace(',', '')
                m, d, y = date.split(' ')
                # Turn the month into a number
                for month, index in months.items():
                    if month == m:
                        m = index
                        break

                # Check if the date is valid
                if not date_validity(m, d):
                    raise ValueError('Not a valid date')

                print(f'{y}-{int(m):02}-{int(d):02}')
                break

        except Exception:
            print('Exception error')
        except ValueError:
            print('ValueError')


def date_validity(m, d):
    # Return true if valid false if invalid
    if int(m) > 12 or int(d) > 31:
        return False
    else:
        return True


main()
