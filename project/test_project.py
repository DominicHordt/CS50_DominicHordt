from project import *
import pytest

# URL class tests
def test_url_parser():
    url = "https://cs50.harvard.edu/python/2022/project/"
    assert URLParser.parse_url(url) == "cs50.harvard.edu"
    with pytest.raises(ValueError) as e:
        assert URLParser.parse_url('5') == e

def test_validate_string():
    url1 = "https://cs50.harvard.edu/python/2022/project/"
    url2 = "cs50.harvard.edu"
    non_url = "stunning-space-adventure"
    assert URLParser.validate_string(url1) == "https://cs50.harvard.edu/python/2022/project/"
    assert URLParser.validate_string(url2) == "https://cs50.harvard.edu"
    with pytest.raises(ValueError) as e:
        assert URLParser.validate_string(non_url) == e

# Email class tests
def test_is_empty():
    with pytest.raises(ValueError) as e:
        assert Email('') == e

def test_email_validator():
    email1 = Email("david@harvard.edu")
    email2 = Email("david_malan")
    assert email1.email_validator() == "david@harvard.edu"
    with pytest.raises(ValueError) as e:
        email2.email_validator() == e
