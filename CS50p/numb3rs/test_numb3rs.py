# Code created by Pepijn Weitzel

from numb3rs import validate

def test_nothing():
    assert validate("") == False

def test_rest():
    assert validate("2.3.4.5") == True
    assert validate("266.234.223.12") == False
    assert validate("221.266.266.266") == False
