import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Check if there is a iframe element
    if iframe := re.search(r"<iframe (.*)></iframe>", s):
        # Check if there is a src attribute
        if src := re.search(r'src="(.*)"', iframe.group(1)):
            # Return the normal link from the embedded link
            if link := re.search(r'https?://(?:www.)?youtube\.com/embed/(?P<link>.+)', src.group(1)):
                return f'https://youtu.be/{link.group('link')}'
    # Return None if not all of these were True
    return None


if __name__ == "__main__":
    main()
