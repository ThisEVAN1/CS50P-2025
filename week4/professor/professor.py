from random import randint


def main():
    level = get_level()
    amount_of_answers_correct = 0

    # Ask 10 math questions
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        tries = 0

        # While tries is less than 3, ask the user for their answer
        while tries < 3:
            try:
                user_input = int(input(f"{x} + {y} = "))
                if user_input == x + y:
                    amount_of_answers_correct += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1

        # If they tried 3 times already then just give them the answer
        if tries == 3:
            print(f"{x} + {y} = {x + y}")

    print(f"Score: {amount_of_answers_correct}")


def get_level():
    # Check if level is 1, 2, or 3
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    # Generate the amount of digits each int has depending on the level
    if level == 1:
        return randint(0, 9)
    elif level == 2:
        return randint(10, 99)
    elif level == 3:
        return randint(100, 999)


if __name__ == "__main__":
    main()
