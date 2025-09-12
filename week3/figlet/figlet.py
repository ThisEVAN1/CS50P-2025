from pyfiglet import Figlet
from random import choice
import sys


if len(sys.argv) == 1 or len(sys.argv) == 3:
    figlet = Figlet()

    if len(sys.argv) == 3:
        if not sys.argv[1] == "-f" or sys.argv[1] == "--font":
            sys.exit('First argument is\'nt "-f" or "--font"')
        elif not sys.argv[2] in figlet.getFonts():
            sys.exit("Incorrect font name")
        else:
            # Set the font to be whatever the user put then print it
            s = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(s))
    else:
        # Set the font to be random then print it
        s = input("Input: ")
        figlet.setFont(font=choice(figlet.getFonts()))
        print(figlet.renderText(s))
else:
    sys.exit("Only 0 or 2 command-line arguments allowed")
