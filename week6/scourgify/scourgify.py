import sys
import csv


try:
    if len(sys.argv) != 3:
        sys.exit('Need 2 files')

    # Read and write the file
    with open(sys.argv[1], 'r', newline = '') as file, open(sys.argv[2], 'w') as write_file:
        # Read the file
        reader = csv.DictReader(file)
        writer = csv.DictWriter(write_file, fieldnames=['first', 'last', 'house'])
        writer.writeheader()
        
        # Loop through every line that was read
        for row in reader:
            last, first = row['name'].split(', ')

            # Write it into the new file
            writer.writerow({
                'first': first,
                'last': last,
                'house': row['house']
            })

except FileNotFoundError:
    sys.exit('File not found')
