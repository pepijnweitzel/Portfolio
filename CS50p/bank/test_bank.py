# Code created by Pepijn Weitzel
from bank import value

def test_hello():
    assert value("hello") == 0

def test_start_h():
    assert value("hey") == 20

def test_nothing():
    assert value("bye") == 100