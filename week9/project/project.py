import csv
import argparse
from tabulate import tabulate
import sys
import time


class Quiz:
    data = []

    def __init__(self, file):
        self._file = file
        if not file.endswith('.csv'):
            raise FileNotFoundError('Didn\'t find a csv file')

    def __str__(self):
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
                    headers[0]: row[headers[0]],
                    headers[1]: row[headers[1]],
                    'answered': False
                })
         


def main():
    quiz = Quiz('example.csv')
    quiz.create_dict()
    print(quiz)


if __name__ == '__main__':
    main()