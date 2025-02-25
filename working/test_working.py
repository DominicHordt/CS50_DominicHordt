from working import convert
import pytest

def test_no_min():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_min():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_long_day():
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"

def test_night_time():
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"

def test_borders():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_invalid_time():
    with pytest.raises(ValueError):
        assert convert("9:60 AM to 5:60 PM")

def test_invalid_format_no_min():
    with pytest.raises(ValueError):
        assert convert("9 AM - 5 PM")

def test_invalid_format():
    with pytest.raises(ValueError):
        assert convert("09:00 AM - 17:00 PM")

def test_no_am_pm():
    with pytest.raises(ValueError):
        assert convert("09:00 to 17:00")

def test_no_space():
    with pytest.raises(ValueError):
        assert convert("9AM to 5PM")
