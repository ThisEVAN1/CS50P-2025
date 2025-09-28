import pytest
from um import count


def test_count():
    assert count('um') == 1
    assert count('um um um') == 3
    assert count('um, um') == 2
    assert count('') == 0
    assert count('yummy') == 0
    assert count('umbrella') == 0
    assert count('I like um... dogs!') == 1
    assert count('I LOVE AH.. UHH.. UM... UM... DOGS!!!') == 2
    assert count('Um hi to whoever is looking at this!') == 1
