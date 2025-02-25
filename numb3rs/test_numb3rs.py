from numb3rs import validate
import pytest

def test_true():
    assert validate("192.168.45.7") == True

def test_invalid_octets():
    assert validate("123.456.258.1") == False

def test_word():
    assert validate("Cat") == False

def test_full_octets():
    assert validate("255.255.255.255") == True

def test_non_four():
    assert validate("43.43") == False

def test_one_num():
    assert validate("4") == False

def test_five_octets():
    assert validate("12.12.12.12.12") == False

def test_int():
    with pytest.raises(TypeError):
        assert validate(5)
