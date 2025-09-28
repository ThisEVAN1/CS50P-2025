import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    amount = 0
    if match := re.findall(r'\bum\b', s, re.IGNORECASE):
        amount = len(match)
    return amount


if __name__ == "__main__":
    main()
