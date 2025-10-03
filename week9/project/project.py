import csv
from tabulate import tabulate
import sys
import time
import re
import threading


timeout_event = threading.Event()


class Quiz:
    data = []

    def __init__(self, file):
        self._file = file
        if not file.endswith('.csv'):
            sys.exit('Didn\'t find a csv file')

    def __str__(self):
        '''
        Return the data dict
        '''
        return str(self.data)

    def create_dict(self):
        """
+       Reads the CSV file specified by self._file, checks for exactly two headers,
+       and populates the Quiz.data list with dictionaries containing the question,
+       answer, and an 'answered' flag set to False.
+       Raises ValueError if the CSV does not have exactly two headers.
+       """
        # Read the csv file
        with open(self._file, 'r') as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames
            if len(headers) != 2:
                raise sys.exit('2 headers required')
            for row in reader:
                # Append the question and answer to the dict and also set answered to false
                Quiz.data.append({
                    headers[0]: row[headers[0]].strip().lower(),
                    headers[1]: row[headers[1]].strip().lower(),
                    'answered': False
                })
         

def main():
    time_limit = input('Time limit (example: 3:25 for 3 min and 25 secs): ').strip().lower()
    time_limit = validate_countdown(time_limit)

    timer_thread = threading.Thread(target=countdown, args=(time_limit,), daemon=True)
    timer_thread.start()

    quiz = Quiz('example.csv')
    quiz.create_dict()

    while not timeout_event.is_set():
        try:
            #print(quiz)
            s = input('s: ')
            b = input('b: ')
        except KeyboardInterrupt:
            # Print out the user's score
            print('something')
            sys.exit()


def validate_countdown(time_limit):
    if time_limit == 'inf':
        return 999999
    elif match := re.search(r'^(\d*):(0\d|\d{2})$', time_limit):
        min = int(match.group(1))
        secs = int(match.group(2))
        return min * 60 + secs
    else:
        sys.exit('Invalid format')


def countdown(time_limit):
    while time_limit > 0:
        time.sleep(1)
        time_limit -= 1
    timeout_event.set()


if __name__ == '__main__':
    main()