from um import count

def test_one_occur():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1

def test_two_occur():
    assert count("Um, thanks, um...") == 2
    assert count("um, hello, um, world") == 2
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2

def test_none():
    assert count("yum") == 0
    assert count("yummy") == 0
