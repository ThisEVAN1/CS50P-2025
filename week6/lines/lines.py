import sys


try:
    lines_count = 0

    # Check if there are only 2 command line arguments
    if len(sys.argv) != 2:
        sys.exit("Only 1 file")
    # Check if the file is a .py file
    if sys.argv[1].find(".py") == -1:
        sys.exit("Only a .py file")

    # Read all the lines in the file
    with open(sys.argv[1], "r") as file:
        # For every line, strip it and then add 1 to lines_count if it isn't a blank line or a comment line
        for line in file:
            line = line.rstrip()
            if line == "":
                continue
            elif line.lstrip()[0] == "#":
                continue
            else:
                lines_count += 1

    print(lines_count)
except FileNotFoundError:
    sys.exit("File not found")
