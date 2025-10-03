import csv
from tabulate import tabulate
import sys
import time
import re


class Quiz:
    data = []

    def __init__(self, file, duration):
        self._file = file
        self._duration = duration
        if not file.endswith('.csv'):
            raise FileNotFoundError('Didn\'t find a csv file')

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
                raise ValueError('2 headers required')
            for row in reader:
                # Append the question and answer to the dict and also set answered to false
                Quiz.data.append({
                    headers[0]: row[headers[0]].strip().lower(),
                    headers[1]: row[headers[1]].strip().lower(),
                    'answered': False
                })
         

def main():
    
    quiz = Quiz('example.csv', )
    quiz.create_dict()
    print(quiz)


def countdown():
    time_limit = int(input('Time limit (example: 3:25 for 3 min and 25 secs): ').strip().lower())
    if time_limit == 'inf':
        return 999999
    elif match := re.search(r'(\d)*:(0\d|\d{2})', time_limit):
        min = eval(match.group(1))
        sec = eval(match.group(2))

        return min * 60 + sec
    else:
        raise ValueError('Invalid format')


if __name__ == '__main__':
    main()