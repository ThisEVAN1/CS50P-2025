import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # All numbers between each . has to be 0-255
    from0to255 = r"(2[0-4]\d|25[0-5]|1\d{2}|\d{2}|\d)"
    pattern = rf"^{from0to255}\.{from0to255}\.{from0to255}\.{from0to255}$"
    if match := re.search(pattern, ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
