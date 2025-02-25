from seasons import print_date, input_date
from datetime import date
import pytest

def test_print():
    assert print_date(34) == "Thirty-four minutes"

def test_date():
    assert input_date("2032-01-01") == date(2032, 1, 1)

def test_wrong_date():
    with pytest.raises(SystemExit) as exit:
        assert input_date("January 1, 1999") == exit
