import csv
from tabulate import tabulate
import sys
import time
import re
import threading


timeout_event = threading.Event()


class Quiz:
    # All the data
    data = []
    # The data in which the player is supposed to see
    visual_data = []

    def __init__(self, file):
        self._file = file
        if not file.endswith('.csv'):
            sys.exit('Didn\'t find a csv file')

    def __str__(self):
        '''
        Return the data dict.
        '''
        return str(tabulate(self.visual_data, headers='keys', tablefmt='grid'))

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

    def change_visual_data(self):
        '''
        Change to visual_data.
        If the question has been answered then add the answer to the table.
        If it hasn't been answered then make it so it shows nothing on the answer part of the table.
        '''
        for dict in self.data:
            # Append the question to the table and also the answer but only if it has already been answered correctly.
            if self.data[dict['answered']] == True:
                # Append the question and answer
                Quiz.visual_data.append({
                    'question': dict['question'],
                    'answer': dict['answer']
                })
            else:
                # Append the question but nothing as the answer
                Quiz.visual_data.append({
                    'question': dict['question'],
                    'answer': '???'
                })


def main():
    # Gets the time and makes sure it is in the right format
    time_limit = input('Time limit: ').strip().lower()
    time_limit = validate_countdown(time_limit)

    # Creates a thread so that the timer can count down without pausing the main funciton
    timer_thread = threading.Thread(target=countdown, args=(time_limit,), daemon=True)
    timer_thread.start()

    # Starts the quiz
    quiz = Quiz('example.csv')
    quiz.create_dict()
    quiz.change_visual_data()

    while not timeout_event.is_set():
        try:
            print(quiz)
            print(quiz.visual_data)
            sys.exit()
        except KeyboardInterrupt:
            # Print out the user's score
            print('something')
            sys.exit()


def validate_countdown(time_limit):
    '''
    Makes sure that the time is in the valid format.
    '''
    if time_limit == 'inf':
        return 999999
    elif match := re.search(r'^(\d*):(0\d|\d{2})$', time_limit):
        min = int(match.group(1))
        secs = int(match.group(2))
        return min * 60 + secs
    else:
        sys.exit('Invalid format')


def countdown(time_limit):
    '''
    Creates a timer that counts down from the amount of time given.
    '''
    while time_limit > 0:
        time.sleep(1)
        time_limit -= 1
    timeout_event.set()


if __name__ == '__main__':
    main()