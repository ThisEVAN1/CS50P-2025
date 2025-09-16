def main():
    greeting = input("Greeting: ").strip()
    print(value(greeting))


def value(greeting):
    if greeting.lower().find("hello") == 0:
        return "$0"
    elif greeting.lower().find("h") == 0:
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()
