import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Make sure the time is valid
    time = r"(?:1[0-2]|\d)(?::[0-5]\d)?"
    pattern = rf"^(?P<time1>{time}) (?P<ampm1>AM|PM) (?:to )?(?P<time2>{time}) (?P<ampm2>AM|PM)$"
    if match := re.search(pattern, s):
        hr24time = ""
        for i in [1, 2]:
            timei = match.group(f"time{i}")
            ampmi = match.group(f"ampm{i}")
            hour = int(timei.split(":")[0])
            # Hours and minutes
            if hour == 12:
                hour = 0
            if len(timei) > 2:
                minute = f"{int(timei.split(':')[1]):02}"
            else:
                minute = "00"

            # Add the time to hr24time depending if it is AM or PM
            if ampmi == "AM":
                # Adds time of the 12 hour time converted to 24 hour time for AM
                hr24time += f"{hour:02}:{minute}"
            else:
                # Add 12 hours since it is PM
                hr24time += f"{hour + 12:02}:{minute}"
            if i == 1:
                hr24time += " to "
        return hr24time
    else:
        raise ValueError()


if __name__ == "__main__":
    main()
