from twttr import shorten

def test_word():
    assert shorten("Word") == "Wrd"

def test_vowels_only():
    assert shorten("aeiou") == ""

def test_cons_only():
    assert shorten("fghj") == "fghj"

def test_empty():
    assert shorten("") == ""

def test_numbers():
    assert shorten("1234") == "1234"

def test_punctuation():
    assert shorten("Hello.") == "Hll."

def test_cap_vowel():
    assert shorten("Aloha") == "lh"
