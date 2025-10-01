from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar(-0.1)
    with pytest.raises(TypeError):
        Jar('hi')
    with pytest.raises(ValueError):
        Jar(-99999)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    try:
        Jar().deposit(5)
        Jar().deposit(12)
        Jar(100).deposit(50)
    except ValueError:
        pytest.fail('ValueError was raised')

    with pytest.raises(ValueError):
        Jar().deposit(13)
    with pytest.raises(ValueError):
        Jar(100).deposit(101)
    with pytest.raises(ValueError):
        Jar(0).deposit(1)


def test_withdraw():
    try:
        Jar(12, 5).withdraw(5)
        Jar(0, 0).withdraw(0)
        Jar(100, 50).withdraw(25)
    except ValueError:
        pytest.fail('ValueError was raised')

    with pytest.raises(ValueError):
        Jar(12, 12).withdraw(13)
    with pytest.raises(ValueError):
        Jar(100, 100).withdraw(101)
    with pytest.raises(ValueError):
        Jar(0).withdraw(1)
