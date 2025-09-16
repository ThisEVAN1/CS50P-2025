from bank import value


def test_value_lowercase():
    assert value("hello") == "$0"
    assert value("hi") == "$20"
    assert value("What's up?") == "$100"


def test_value_uppercase():
    assert value("Hello") == "$0"
    assert value("Hi") == "$20"
    assert value("What's up?") == "$100"
