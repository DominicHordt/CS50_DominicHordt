from plates import is_valid

def test_valid():
    assert is_valid("CS50") == True

def test_starts_with_zero():
    assert is_valid("CS05") == False

def test_one_letter():
    assert is_valid("C") == False

def test_middle_nums():
    assert is_valid("AAA22A") == False

def test_punctuation():
    assert is_valid("AAA_22") == False

def test_long_name():
    assert is_valid("OUTATIME") == False

def test_digits():
    assert is_valid("44") == False
