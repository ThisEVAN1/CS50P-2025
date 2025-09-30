from datetime import date
import inflect
import re
import sys


def main():
    try:
        # Check if it is in YYYY-MM-DD format
        if birthdate := re.search(r'^(?:\d+-){2}\d+$', input('Date of Birth: ')):
            # Split the date into year, month, and day
            year, month, day = map(int, birthdate.group(0).split('-'))
            converted_date = convert(date(year, month, day), date.today())
            p = inflect.engine()
            print(f'{p.number_to_words(converted_date, andword='').capitalize()} {p.plural('minute', converted_date)}')
        else:
            raise ValueError()
    except ValueError:
        sys.exit('Invalid date')


def convert(birthdate, current_date):
    # Get the amount of minutes between the two dates
    time_alive = (current_date - birthdate).days * 24 * 60
    return time_alive



if __name__ == "__main__":
    main()
