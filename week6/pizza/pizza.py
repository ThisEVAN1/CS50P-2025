import csv
import sys
from tabulate import tabulate


data = []

try:
    # Check if there are 2 cmd line arguments
    if len(sys.argv) != 2:
        sys.exit('Only 1 file')
    # Checks if it is a .csv file
    if sys.argv[1].find('.csv') == -1:
        sys.exit('Needs to be a .csv file')

    # Read the file
    with open(sys.argv[1], 'r') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        # Append the data
        for row in f:
            # Remove the \n at the end of each row string and then split them up into arrays
            row = row.replace('\n', '')
            row = row.split(',')
            data.append({
                headers[0]: row[0],
                headers[1]: row[1],
                headers[2]: row[2]
            })

    print(tabulate(data, headers='keys', tablefmt='grid'))
except FileNotFoundError:
    sys.exit('File does not exist')
