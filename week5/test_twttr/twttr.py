def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(word):
    return (
        word.replace("A", "")
        .replace("E", "")
        .replace("I", "")
        .replace("O", "")
        .replace("U", "")
        .replace("a", "")
        .replace("e", "")
        .replace("i", "")
        .replace("o", "")
        .replace("u", "")
    )


if __name__ == "__main__":
    main()
