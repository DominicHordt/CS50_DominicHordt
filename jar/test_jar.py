from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar1 = Jar(20)
    assert jar1.capacity == 20
    with pytest.raises(ValueError) as error:
        assert Jar(-20) == error


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(7)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError) as error:
        assert jar.deposit(17) == error


def test_withdraw():
    jar = Jar()
    jar.deposit(7)
    jar.withdraw(6)
    assert str(jar) == "🍪"
    with pytest.raises(ValueError) as error:
        assert jar.withdraw(17) == error
